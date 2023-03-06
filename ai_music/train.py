import torch
from dataset import load
from model import AI


ai = AI(batch_size=16, device=torch.device("cuda"))
loader = load(batch_size=16)

for i in range(100):
    for data in loader:
        loss = ai.pre_train(data)
        print("pre", loss)

ai.eval_and_play()

for i in range(100):
    for i in range(2):
        for data in loader:
            loss = ai.pre_train(data)
            print("pre", loss)

    for i in range(2):
        for data in loader:
            loss = ai.train(data)
            print("dis", loss)

ai.eval_and_play()




