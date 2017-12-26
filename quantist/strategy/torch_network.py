# -*- coding: utf-8 -*-

# quantist
# 
# Copyright 2017-2018 Pan Liu
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
# by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Unless required

""" 
Author: liupan 
"""

"""
Description:
"""

import torch
import torch.nn as nn
import torch.autograd as autograd
from torch.autograd import Variable
import numpy as np


class Network(nn.Module):
    def __init__(self, n_prev, h0, c0):
        super(Network, self).__init__()
        self.n_prev = n_prev
        self.h0 = h0
        self.c0 = c0

        self.LSTM_layer = nn.LSTM(self.n_prev, self.h0, self.c0)
        self.fc1 = nn.Linear(self.h0, 300)
        self.fc2 = nn.Linear(300, 250)
        self.fc3 = nn.Linear(250, 150)
        self.fc4 = nn.Linear(150, 100)
        self.fc5 = nn.Linear(100, 50)
        self.fc6 = nn.Linear(50, 20)
        self.fc7 = nn.Linear(20, 1)

    def forward(self, x):
        output, hn = self.LSTM_layer(x)
        out = self.fc1(output)
        out = self.fc2(out)
        out = self.fc3(out)
        out = self.fc4(out)
        out = self.fc5(out)
        out = self.fc6(out)
        predict = self.fc7(out)
        return predict

# model = Network(1, 100, 50)
# a = np.array([1.5])
# a = Variable(torch.from_numpy(a)).float()
# a = a.view(1,1,1)
# print(model(a))
