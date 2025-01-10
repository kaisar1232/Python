import pandas as pd
import numpy as np

# Define the data for df1 and df2
df1 = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df2 = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

# Combine the data into a dictionary
data = {
    'Item1': df1,
    'Item2': df2}

# Create a Panel (deprecated in pandas, consider using a different approach)
p = pd.Panel(data)
print(p)
