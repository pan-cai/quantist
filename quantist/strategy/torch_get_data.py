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

import quandl
import numpy as np
import torch
from torch.autograd import Variable




# Get the data dynamics as below
# mydata_ = quandl.get("EIA/PET_RWTC_D")
# plt.xlabel("date")
# plt.ylabel("Price")
# plt.plot(mydata_)
# plt.show()

class Get_data:
    def __init__(self, n_prev, data_code):
        self.n_prev = n_prev
        self.data = quandl.get(data_code, returns="numpy")
        self.X = []
        self.Y = []

    def get_data(self, today):
        for k in range(self.n_prev):
            temp = self.data[today-self.n_prev+k][1]
            print(type(temp))#numpy.float64
            print(type(self.X)) # list
            #temp = temp.item()
            print(type(temp))
            self.X.append(temp)
        print("--------")
        print(self.X)
        self.Y.append(self.data[today][1])
        self.X = Variable(torch.from_numpy(np.array(self.X))).float().view(1,1,self.n_prev)
        self.Y = Variable(torch.from_numpy(np.array(self.Y))).float().view(1,1,1)
        return self.X, self.Y

    def get_raw_data(self):
        return self.data


# check data form
# data_code = "EIA/PET_RWTC_D"
# model = Get_data(5, data_code)
# a, b = model.get_data(60)
# print(a)
