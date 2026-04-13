# Program9 unit-2
# Missing Data
import pandas as pd
df=pd.read_csv('airlines.csv')
print('Missing Values:')
print(df.isnull().sum())
# Removing all null data
ds=df.dropna()
print('After removing Null values:')
print(ds.shape)
