__author__ = 'nehaavishwa'

import numpy as np
from scipy.stats import scoreatpercentile
FILEPATH = r'/home/nehaavishwa/PycharmProjects/DataWrangle/Files/MDR-TB_burden_estimates_2015-11-01.csv'
data = np.loadtxt(FILEPATH, dtype=float, delimiter=',', usecols=(8,),skiprows=1, unpack=True)
print("Max Method", data.max())
print("Max Function", np.max(data))
print("================================")
print("Min Method", data.min())
print("Min Function", np.min(data))
print("================================")
print("Mean method", data.mean())
print("Mean function", np.mean(data))

