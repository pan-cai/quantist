data_path = "../quantist/data/pool/"

import pandas as pd
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import math
import numpy
import matplotlib.pyplot as plt

companies = 'GOOG'
look_back = 1


def get_historical_close_data(name):
    url = "https://www.google.com/finance/historical?q=%s&startdate=01-Jan-2000&output=csv" % name

    data = pd.read_csv(url)
    data = data.loc[:, ('Date', 'Close')]
    data = data.sort_index(ascending=False)
    return data


def normalization(data):
    scaler = MinMaxScaler(feature_range=(0, 1))
    data_norm = scaler.fit_transform(data)

    return data_norm


def de_normalization(data, new_data):
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaler.fit_transform(data)
    unormalized = scaler.inverse_transform(new_data)

    return unormalized


def split_train_test(data):
    # split into train and test sets
    train_size = int(len(data) * 0.67)
    train, test = data[0:train_size, ], data[train_size:len(data), ]
    return train, test

def create_dataset(dataset, lookback):
    dataX, dataY = [], []
    for i in range(len(dataset)-lookback-1):
        a = dataset[i:(i+lookback), ]
        dataX.append(a)
        dataY.append(dataset[i + lookback, ])
    return numpy.array(dataX), numpy.array(dataY)

#dataset = get_historical_close_data(companies)
dataset = pd.read_excel(data_path + 'sh2.xls')

dataset_norm = normalization(dataset['close'].values.reshape(-1,1))

train_dataset, test_dataset = split_train_test(dataset_norm)

train_X, train_y = create_dataset(train_dataset, look_back)

test_X, test_y = create_dataset(test_dataset,look_back)

train_X = numpy.reshape(train_X, (train_X.shape[0], 1 , train_X.shape[1]))
test_X = numpy.reshape(test_X, (test_X.shape[0], 1, test_X.shape[1]))

model = Sequential()
model.add(LSTM(32, input_shape=(None,1)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(train_X, train_y, epochs=3, batch_size=1, verbose=2)

trainPredict = model.predict(train_X)
testPredict = model.predict(test_X)

trainPredict = de_normalization(dataset['close'].values.reshape(-1,1), trainPredict)
train_y = de_normalization(dataset['close'].values.reshape(-1,1),train_y)
testPredict = de_normalization(dataset['close'].values.reshape(-1,1), testPredict)
test_y = de_normalization(dataset['close'].values.reshape(-1,1),test_y)

trainScore = math.sqrt(mean_squared_error(train_y, trainPredict[:,0]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(test_y, testPredict[:,0]))
print('Test Score: %.2f RMSE' % (testScore))

trainPredictPlot = numpy.empty_like(dataset_norm)
trainPredictPlot[:, ] = numpy.nan

trainPredictPlot[look_back:len(trainPredict)+look_back, ] = trainPredict[:,0].reshape(-1,1)
# shift test predictions for plotting
testPredictPlot = numpy.empty_like(dataset_norm)
testPredictPlot[:,] = numpy.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset['close'])-1, ] = testPredict[:,0].reshape(-1,1)
# plot baseline and predictions.reshape(-1,1)
plt.plot(de_normalization(dataset['close'].values.reshape(-1,1),dataset_norm))
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.show()

