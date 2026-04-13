# Program2 unit-2
#First Version
import pandas as pd
# Read dataset
#df=pd.read_csv('auto-mpg.csv')
df=pd.read_csv('auto-mpg.csv',na_values='?')

# Find numeric attributes
print('Numeric Attributes:')
print(df.select_dtypes(include='number').columns)

# Find categorical attributes
print('\nCategorical Attributes:')
print(df.select_dtypes(include=['object','string']).columns)
