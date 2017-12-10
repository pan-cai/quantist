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
Create date: 
"""

"""
Description:
"""

import tushare as ts
import pandas as pd
from quantist.utils import change_data_form as cdf


class GetDataFromTushare(object):
    """
    Code is the stock code
    If save is True, save the data, else return the stock data. Default don't save
    Must write sava is true or false
    """

    def getStockData(code=None, start=None, end=None, save=True):
        PATH = "./pool/"
        data = ts.get_hist_data(str(code), start=None, end=None);
        #Change the form
        # data.reset_index(inplace=True)
        # data['date'] = pd.to_datetime(data['date'])
        # data = data.set_index('date')
        data = cdf.ChangeDataForm.to_day_form(data)
        # Save data
        if save:
            data.to_csv(PATH + "s" + code + ".csv")
            print("Save " + code)
            return data
        # Don't sava data
        else:
            return data

    def getSavedStock(code=None):
        PATH = "./pool/" + "s" + code + ".csv"
        try:
            data = pd.read_csv(PATH)
            print("Get data ...")
            return data
        except:
            try:
                print('Data doses not exit in pool, get it from tushare ... ')
                data = ts.get_hist_data(str(code))
                return data
            except:
                print('Data doses not exit')

    def getNlpData(self):
        pass


"""
# Simple test
"""

""""""
# Test
"""
data = GetDataFromTushare.getStockData('600848', save=True)
print(data[:3])
"""
data = GetDataFromTushare.getSavedStock('600848')
print(data[:3])

