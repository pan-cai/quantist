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

import talib
from unittest import TestCase
import quantist.global_list as gl

SH_DATA = gl.TEST_SH_PRICES
CLOSE_PRICES = SH_DATA['close'].values
OPEN_PRICES = SH_DATA['open'].values
HIGH_PRICES = SH_DATA['high'].values
LOW_PRICES = SH_DATA['low'].values
VOLUMES = SH_DATA['volume'].values


class TestTalib(TestCase):
    def test_CCI(self):
        ccitalib = talib.CCI(HIGH_PRICES, LOW_PRICES, CLOSE_PRICES, timeperiod=10)[-1]
        print(ccitalib)  # 68.8081586162

    def test_MA(self):
        ma5 = talib.MA(CLOSE_PRICES)
        print(ma5)
        """
        [           nan            nan            nan            nan            nan
            nan            nan            nan            nan            nan
            nan            nan            nan            nan            nan
            nan            nan            nan            nan            nan
            nan            nan            nan            nan            nan
            nan            nan            nan            nan  3243.08346667
            3246.5293      3247.28223333  3246.74856667  3246.40483333  3246.6582 ...]
        """

    def test_CMO(self):
        cmo = talib.CMO(CLOSE_PRICES, timeperiod=14)
        print(cmo)
        """
        [             nan              nan              nan              nan
              nan              nan              nan              nan
              nan              nan              nan              nan
              nan              nan   5.32573621e+01   5.60318756e+01 ... ]
        """

    def test_SMA(self):
        ma3 = talib.SMA(CLOSE_PRICES, timeperiod=3)
        print(ma3[:5])  # [           nan            nan  3285.33333333  3289.89666667  3302.42      ]

# t = TestTalib()
# t.test_SMA()
