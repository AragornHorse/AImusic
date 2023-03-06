from torch.utils.data import DataLoader, Dataset
import numpy as np
import torch

class Data(Dataset):
    def __init__(self):
        self.data = np.load("data.npy")

    def __getitem__(self, item):
        return self.data[item]

    def __len__(self):
        return self.data.shape[0]


def load(batch_size=16):
    return DataLoader(Data(), batch_size=batch_size, shuffle=True)








