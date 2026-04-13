# Program2 unit-2
#Second Version
import pandas as pd
# Read dataset
df=pd.read_csv('auto-mpg.csv',na_values='?')

# Numeric columns
num_cols=df.select_dtypes(include='number').columns

# Categorical columns
cat_cols=df.select_dtypes(exclude='number').columns

print('Numeric Attributes:')
print(list(num_cols))

print('\nCategorical Attributes:')
print(list(cat_cols))
