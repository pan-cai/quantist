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
from quantist.data.get_and_save_data import GetDataFromTushare as gdft
from quantist.utils import change_data_form as cdf
import matplotlib.pyplot as plt
import seaborn as sns
import tushare as ts


class Plotter(object):
    """
    Plot basic parameter
    parameter: close, p_change
    Example:
        path = "../data/pool/"
        Plotter.plot_single_stock(path, 'close','600848')
    """
    def plot_single_stock(path, parameter, code=None,):
        data_gdft = gdft.getSavedStock(path, code)
        # Formed the data
        data = cdf.ChangeDataForm.to_day_form(data_gdft)
        data[parameter].plot(label=code)
        plt.legend(loc='best')
        plt.title(code)
        plt.show()


# Sample test
path = "../data/pool/"
Plotter.plot_single_stock(path, 'close','600327')

# plt.show(plt.plot([x for x in range(5)]))
