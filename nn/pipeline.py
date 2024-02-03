import os
import torch

from torch.utils.data import Dataset, DataLoader
import torch.nn as nn

import numpy as np


class DigitsDataset(Dataset):
    def __init__(self, X, y) -> None:
        super().__init__()
        self.X = X
        self.y = y

    def __getitem__(self, index):
        return self.X[index].astype(np.float32), self.y[index]
    
    def __len__(self):
        return self.X.shape[0]
    

class Pipeline:
    model_path = 'models'

    def __init__(self, X, y, expname='default'):
        self.X = X
        self.y = y
        self.dataset = DigitsDataset(X, y)

        self.net = nn.Sequential(
            nn.Linear(64, 200),
            nn.ReLU(),
            nn.Linear(200, 10)
        )

        self.loss = torch.nn.CrossEntropyLoss()
        self.dataloader = DataLoader(self.dataset, batch_size=100, shuffle=True)

        self.optim = torch.optim.Adam(params=self.net.parameters())

        self.experiment_path = os.path.join(self.model_path, expname)
        os.makedirs(self.experiment_path, exist_ok=True)

    def train_epoch(self, epoch):
        for index, item in enumerate(self.dataloader):
            self.optim.zero_grad()

            batch_x, batch_y = item
            # print(batch_x)
            logits  = self.net(batch_x)

            loss_fn = self.loss(logits, batch_y)

            loss_fn.backward()
            self.optim.step()

        self.dump_model(epoch)
        

        return loss_fn.item()

    def dump_model(self, epoch):
        torch.save(
            self.net.state_dict(),
            os.path.join(self.experiment_path, f'{epoch}.pt')
        )

