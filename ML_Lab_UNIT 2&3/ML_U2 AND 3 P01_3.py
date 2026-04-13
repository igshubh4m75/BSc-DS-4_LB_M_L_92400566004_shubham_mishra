# Program1 unit-2
# Third version
import pandas as pd

#Read CSV file
df1=pd.read_csv('auto-mpg.csv')
print('CSV File:')
print(df1.head())

#Read Text file
df2=pd.read_csv('auto-mpg.txt',delim_whitespace=True)
print('\nText File:')
print(df2.head())

#Read JSON file
df3=pd.read_json('auto-mpg.json')
print('\nJSON File:')
print(df3.head())

#Read XML file
df4=pd.read_xml('auto-mpg.xml')
print('\nXML File:')
print(df4.head())
