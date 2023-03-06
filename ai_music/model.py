import torch
import torch.nn as nn
import torch.optim as optim
from Music import Piano
import numpy as np

class Attention(nn.Module):
    def __init__(self, in_size, v_size, q_size=32, bias=True, act_func=None):
        super(Attention, self).__init__()
        self.q_fc = nn.Linear(in_size, q_size, bias=bias)
        self.k_fc = nn.Linear(in_size, q_size, bias=bias)
        self.v_fc = nn.Linear(in_size, v_size, bias=bias)
        self.act_func = act_func if act_func is not None else nn.Tanh()

    def forward(self, x):    # b, s, in
        q = self.q_fc(x)   # b, s, q
        k = self.k_fc(x)   # b, s, q
        v = self.v_fc(x)   # b, s, v
        attn = torch.softmax(q @ torch.transpose(k, dim0=-1, dim1=-2), dim=-1)  # b, s, s
        out = attn @ v  # b, s, v
        out = self.act_func(out)
        return out


class Generator(nn.Module):
    def __init__(self, in_size=None):
        super(Generator, self).__init__()
        if in_size is None:
            in_size = [-1, 30, 4]

        self.in_size = in_size


        self.attn1 = Attention(in_size[-1], 21, 16, True)
        self.attn2 = Attention(in_size[-1], 11, 16, True)

    def forward(self, x):
        num = self.attn1(x)
        t = self.attn2(x)
        return num, t



# class Generator(nn.Module):
#     def __init__(self, in_size=None):
#         super(Generator, self).__init__()
#
#         if in_size is None:
#             in_size = [-1, 30, 4]
#
#         self.in_size = in_size
#         self.fc1 = nn.Sequential(
#             nn.Linear(in_size[-1], 16),   # b, s, 16
#             nn.LeakyReLU(inplace=True)
#         )
#         self.attn1 = Attention(16, 32, 16, True)  # b, s, 32
#         self.lstm1 = nn.LSTM(input_size=32, hidden_size=32, num_layers=2, dropout=0.4, batch_first=True, bidirectional=False)
#         self.attn2 = Attention(32, 32, 32, True)
#         self.fc2 = nn.Sequential(
#             nn.Linear(32, 32, True),
#             nn.Tanh(),
#             nn.Linear(32, 32, True)
#         )
#         self.shortcut2 = nn.Linear(32, 32, True)
#         self.attn3 = Attention(32, 32, 32, True)
#         self.num_fc = nn.Sequential(
#             nn.Linear(32, 21, bias=True)
#         )
#         self.t_fc = nn.Sequential(
#             nn.Linear(32, 11, bias=True)
#         )
#
#     def forward(self, x):
#         out = self.fc1(x)
#         out = self.attn1(out)
#         out, _ = self.lstm1(out)
#         out = self.attn2(out)
#         long = self.fc2(out)
#         short = self.shortcut2(out)
#         out = long + short
#         out = self.attn3(out)
#         num = self.num_fc(out)
#         t = self.t_fc(out)
#         # p_num = self.num_sm(num)
#         # p_t = self.t_sm(t)
#         return num, t


class Discriminator(nn.Module):
    def __init__(self, in_size=None):
        super(Discriminator, self).__init__()

        if in_size is None:
            in_size = [-1, 30, 4]

        self.in_size = in_size
        self.num_emb = nn.Sequential(
            nn.Softmax(dim=-1),
            nn.Linear(21, 32, bias=True),
            nn.LeakyReLU(inplace=True)
        )
        self.t_emb = nn.Sequential(
            nn.Softmax(dim=-1),
            nn.Linear(11, 32, bias=True),
            nn.LeakyReLU(inplace=True)
        )

        self.attn = Attention(32, 32, 16, True)
        self.fc1 = nn.Linear(32, 1, True)
        self.fc2 = nn.Linear(in_size[1], 1)
        self.sig = nn.Sigmoid()

    def forward(self, num, t):
        num_h = self.num_emb(num)
        t_h = self.t_emb(t)
        out = num_h + t_h
        out = self.attn(out)
        out = self.fc1(out).squeeze()
        out = self.fc2(out).squeeze()
        out = self.sig(out).squeeze()
        return out


class AI:
    def __init__(self, device=torch.device("cuda"), pretrain_loss_func=None, train_loss_func=None, batch_size=16):
        self.device = device
        self.in_size = [batch_size, 30, 4]
        self.generator = Generator(self.in_size).to(device)
        self.discriminator = Discriminator(in_size=self.in_size).to(device)

        self.pre_loss_func = pretrain_loss_func if pretrain_loss_func is not None else nn.CrossEntropyLoss()
        self.loss_func = train_loss_func if train_loss_func is not None else nn.BCELoss()

        self.g_opt = optim.Adam(self.generator.parameters(), lr=1e-3)
        self.d_opt = optim.Adam(self.generator.parameters(), lr=1e-3)

        self.piano = Piano()

    def train(self, true_music):  # b, s, 2 [num, t]

        num_t_idx = true_music[:, :, 0].squeeze().unsqueeze(-1).long()  # b, s, 1
        t_t_idx = true_music[:, :, 1].squeeze().unsqueeze(-1).long()   # b, s, 1

        num_t = torch.zeros(num_t_idx.size(0), num_t_idx.size(1), 21)
        t_t = torch.zeros(t_t_idx.size(0), t_t_idx.size(1), 11)

        num_t.scatter_(2, num_t_idx, 1)
        t_t.scatter_(2, t_t_idx, 1)

        num_t = num_t.to(self.device)
        t_t = t_t.to(self.device)

        fake_label = torch.zeros(num_t_idx.size(0), device=self.device)
        true_label = torch.ones(true_music.size(0), device=self.device)
        true_label_ = torch.ones(num_t_idx.size(0), device=self.device)

        # noise = torch.randn(self.in_size[0], self.in_size[1], self.in_size[2]).to(self.device)
        noise = torch.ones(num_t_idx.size(0), self.in_size[1], self.in_size[2]).to(self.device) + \
                torch.randn(num_t_idx.size(0), self.in_size[1], self.in_size[2]).to(self.device) * 0.1

        num_f, t_f = self.generator(noise)

        cls_f = self.discriminator(num_f, t_f)
        loss = self.loss_func(cls_f, true_label_)
        self.g_opt.zero_grad()
        self.d_opt.zero_grad()
        loss.backward()
        self.g_opt.step()
        self.d_opt.zero_grad()

        cls_t = self.discriminator(num_t, t_t)
        cls_f = self.discriminator(num_f.detach(), t_f.detach())
        loss = 0.5 * self.loss_func(cls_f, fake_label) + 0.5 * self.loss_func(cls_t, true_label)
        self.d_opt.zero_grad()
        # self.g_opt.zero_grad()
        loss.backward()
        self.d_opt.step()
        # self.g_opt.zero_grad()

        return loss  # discriminator_loss

    def pre_train(self, true_music):  # b, s, 2
        num_t_idx = true_music[:, :, 0].squeeze().to(self.device).long()  # b, s
        t_t_idx = true_music[:, :, 1].squeeze().to(self.device).long()  # b, s

        # noise = torch.randn(num_t_idx.size(0), self.in_size[1], self.in_size[2]).to(self.device)
        noise = torch.ones(num_t_idx.size(0), self.in_size[1], self.in_size[2]).to(self.device)+ \
                torch.randn(num_t_idx.size(0), self.in_size[1], self.in_size[2]).to(self.device) * 0.1

        num_f, t_f = self.generator(noise)

        loss = self.pre_loss_func(num_f.reshape(-1, 21), num_t_idx.reshape(-1)) + \
               self.pre_loss_func(t_f.reshape(-1, 11), t_t_idx.reshape(-1))
        # loss = self.pre_loss_func(torch.transpose(num_f, dim1=-1, dim0=-2), num_t_idx) + \
        #        self.pre_loss_func(torch.transpose(t_f, dim0=-1, dim1=-2), t_t_idx)

        self.g_opt.zero_grad()
        loss.backward()
        self.g_opt.step()

        return loss  # generator_loss

    def eval(self):
        noise = torch.randn(1, self.in_size[1], self.in_size[2]).to(self.device)
        num_f, t_f = self.generator(noise)   # 1, s, 21/11
        num_ = num_f.squeeze()   # s, 21
        t_ = t_f.squeeze()    # s, 11

        num = torch.argmax(num_, -1)  # s
        t = torch.argmax(t_, -1)  # s

        return num.cpu().detach().numpy(), t.cpu().detach().numpy()

    def eval_and_play(self):
        # idx2time = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.5, 3, 4]
        num, t = self.eval()
        # time = []
        # for t_ in t:
        #     time.append(idx2time[t_])
        # print(t)
        self.piano.play(np.array([num, t]))



# md = AI()

# for i in range(100):
#     print(md.train(torch.ones(8, 30, 2, dtype=torch.long)))
    # print(md.eval())

# md.eval_and_play()





