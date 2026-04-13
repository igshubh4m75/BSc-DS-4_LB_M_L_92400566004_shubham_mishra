# Program10 unit-2
# Rescaling data Min-Max
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
df=pd.read_csv('airlines.csv')
numeric_cols=df.select_dtypes(include=['int64','float64'])
scaler=MinMaxScaler()
df[numeric_cols.columns]=scaler.fit_transform(numeric_cols)
print('Rescaled Data:')
print(df.head())
