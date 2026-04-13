# Program1 unit-2
#First Version
import pandas as pd
ds_csv=pd.read_csv('auto-mpg.csv')
print('CSV Data:')
# Default show 5 records
print(ds_csv.head())
#show 10 records
print(ds_csv.head(10).to_string())
#just show columns names
print('\nColumn Names:')
print(ds_csv.columns)


