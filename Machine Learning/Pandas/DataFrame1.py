import pandas as pd

# Creating an empty DataFrame
print("Empty data frame")
df = pd.DataFrame()
print(df)

# Creating a DataFrame from a list
print("Dataframe with list")
data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data)
print(df)

# Creating a DataFrame from a list of lists with specified column names
print("Dataframe with list")
data = [['PPA', 4], ['LB', 3], ['Python', 3], ['Angular', 3]]
df = pd.DataFrame(data, columns=['Name', 'Duration'])
print(df)

# Creating a DataFrame from a dictionary
data = {'Name': ['PPA', 'LB', 'Python', 'Angular'], 'Duration': [4, 3, 3, 3]}
df = pd.DataFrame(data)
print(df)

# Creating a DataFrame from a list of dictionaries
data = [{'Name': 'PPA', 'Duration': 3, 'Fees': 10500},
        {'Name': 'Angular', 'Duration': 3, 'Fees': 10500},
        {'Name': 'Python', 'Fees': 10500}]
df = pd.DataFrame(data)
print(df)

# Creating a DataFrame from a dictionary of Series
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['x', 'y', 'z', 'w'])}

df = pd.DataFrame(d)

# Printing a specific column from the DataFrame
print(df['one'])
