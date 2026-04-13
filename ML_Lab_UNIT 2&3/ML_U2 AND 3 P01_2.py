# Program1 unit-2
#Second Version
import pandas as pd
#Force pandas to show everything
pd.set_option('display.max_columns',None)
pd.set_option('display.width',2000)
pd.set_option('display.expand_frame_repr',False)

#read dataset
ds_csv=pd.read_csv('auto-mpg.csv')

#Display output
print('CSV Data(First 10 Rows-All columns shown):\n')
print(ds_csv.head(10))
print(ds_csv.head(10).to_string())

print('\nColumn Names:\n')
print(ds_csv.columns)
