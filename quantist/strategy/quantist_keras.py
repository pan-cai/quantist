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
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import seaborn as sns

class quantist_keras(object):

    def demo_regressor(self):
        np.random.seed(1337)

        x = np.linspace(-1,1,200)
        np.random.shuffle(x)
        y = 0.5*x + 2 + np.random.normal(0,0.05,(200,))

        plt.scatter(x,y)
        plt.show()

        x_train,y_train = x[:160], y[:160]
        x_test,y_test = x[160:], y[160:]

        model = Sequential()
        model.add(Dense(output_dim=1,units=1))

        model.compile(loss='mse',optimizer='sgd')

        print('training...')
        for step in range(301):
            cost = model.train_on_batch(x_train,y_train)
            if step%100 == 0:
                print('train cost ',cost)

        print('\n testing...')
        cost = model.evaluate(x_test,y_test,batch_size=40)
        print('test cost',cost)
        w,b = model.layers[0].get_weights()
        print('weight=',w,'\n biases=',b)

        y_pred = model.predict(x_test)
        plt.scatter(x_test,y_test)
        plt.plot(x_test,y_pred)
        plt.show()

"""
Sample test
"""
q = quantist_keras()
q.demo_regressor()