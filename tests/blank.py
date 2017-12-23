import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels import regression

class LinearRegression(object):
    def ols_example(self):
        nobs = 20
        X = np.random.random((nobs, 2))
        print(X)
        X = sm.add_constant(X)
        beta = [1, 1., .5]
        #e = np.random.random(nobs)
        # y = np.dot(X, beta)
        y = np.dot(X, beta)
        # e = np.random.random(nobs)
        print("-------x------------------")
        print(X)
        print("-------y------------------")
        print(y)

        results = sm.OLS(y, X).fit()
        print(results.summary())

# Test ols_example
# t = LinearRegression()
# t.ols_example()
# print(t)
# print("----------------------------------------------------")

xx = [x+0.1 for x in range(20)]
print(xx)
print(len(xx))
xx = np.array(xx)
print(len(xx))
print(xx)
yy = [x for x in range(20)]
results = sm.OLS(yy, xx).fit()
print(results)
print(results.summary())
