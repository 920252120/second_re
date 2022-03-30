import pandas as pd
import numpy as np


def evaluate(a, b):
    a = to_array(a)
    b = to_array(b)
    print("MAE:      %.4f\n"
          "MAPE:     %.4f\n"
          "MSE:      %.4f\n"
          "RMSE:     %.4f\n"
          "RSquared: %.4f\n"
          "NRMSE:    %.4f\n"
          "CVRMSE:   %.4f\n"
          %(mae(a, b), mape(a, b), mse(a, b), rmse(a, b), rsquared(a, b), nrmse(a, b), cvrmse(a, b)))

def to_array(series):
    return np.asarray(series)


def mae(a, b):
    mae = (1 / len(a)) * abs(a - b).sum()
    return mae


def mape(a, b):
    c = abs((a - b) / b)
    mape = (1 / len(a)) * c.sum()
    return mape


def mse(a, b):
    MSE = np.square(a - b).sum() / len(a)
    return MSE


def rmse(a, b):
    RMSE = np.sqrt(mse(a, b))
    return RMSE


def rsquared(a, b):
    y_mean = b.mean()
    SSR = np.square(a - y_mean).sum()  # SSR
    SST = np.square(b - y_mean).sum()  # SST
    Rsquared = SSR / SST
    return Rsquared


def nrmse(a, b):
    y_max = b.max()
    y_min = b.min()
    Rmse = np.sqrt(np.square(a - b).sum())
    NRMSE = (1 / len(a)) * (1 / (y_max - y_min)) * Rmse
    return NRMSE


def cvrmse(a, b):
    y_mean = b.mean()
    Rmse = np.sqrt(np.square(a - b).sum())
    CVRMSE = (1 / len(a)) * (1 / y_mean) * Rmse
    return CVRMSE
