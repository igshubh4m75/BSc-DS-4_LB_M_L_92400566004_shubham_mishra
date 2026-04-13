# Program8 unit-2
# Identify Category
import pandas as pd
df=pd.read_csv('airlines.csv')
print('Numeric Columns:')
print(df.select_dtypes(include=['int64','float64']).columns)
print('\n Categorical Columns:')
print(df.select_dtypes(include=['object']).columns)
