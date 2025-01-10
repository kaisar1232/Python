import pandas as pd
import numpy as np

# Creating an empty Series
s = pd.Series()
print(s)

# Creating a Series from a NumPy array
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)
print(s[0])

# Creating a Series with custom index
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data, index=[100, 101, 102, 103])
print(s[100])

# Creating a Series from a dictionary
data = {'a': 0.1, 'b': 1.1, 'c': 2.1}
s = pd.Series(data)
print(s)

# Creating a Series with labeled index
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s['a'])
