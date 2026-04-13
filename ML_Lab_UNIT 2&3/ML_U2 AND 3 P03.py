# Program3 unit-2
import pandas as pd
import numpy as np
# Local dataset
ds=pd.read_csv('auto-mpg.csv')

#replace '?' with Null - Not a Number
ds['horsepower']=ds['horsepower'].replace('?',np.nan)

# convert horsepower to numeric
ds['horsepower']=pd.to_numeric(ds['horsepower'])

# missing values checking
print('Missing Values Before Filling:\n')
print(ds.isnull().sum())

# fill missing values with mean
ds['horsepower']=ds['horsepower'].fillna(ds['horsepower'].mean())

print('\nMissing Values After Filling:\n')
print(ds.isnull().sum())
