__author__ = 'nehaavishwa'

from pandas.io.parsers import read_csv
import numpy as np
import Quandl

df = read_csv(r'/home/nehaavishwa/PycharmProjects/DataWrangle/Files/WHO.csv')

#print(df)

'''print("Shape", df.shape)
print("Length", len(df))

print("Column Header", df.columns)
print("Data types", df.dtypes)'''

country_col = df["Country"]
#print(country_col)
'''print(type(df))
print(type(country_col))'''

'''print("Series Shape", country_col.shape)
print("Series Index", country_col.index)
print("Series Values", country_col.values)
print("Series Names", country_col.name)'''

'''print("Last 2 countries \n", country_col[-2:])
print("Last 2 country type", type(country_col[-2:]))'''

#print("df sign", np.sign(df))
last_col = df.columns[-1]
#print("last df sign column",last_col, np.sign(df[last_col]))
#print(np.sum(df[last_col]- df[last_col].values))

sunspots = Quandl.get("SIDC/SUNSPOTS_A")
print("Head 2", sunspots.head(2))




