# Program4 unit-2
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Load dataset
df=pd.read_csv('auto-mpg.csv')

# Replace '?' and convert horsepower to numeric
df['horsepower']=df['horsepower'].replace('?',np.nan)
df['horsepower']=pd.to_numeric(df['horsepower'])

# Fill missing values with mean
df['horsepower']=df['horsepower'].fillna(df['horsepower'].mean())

# Select numeric columns only
num_cols=df.select_dtypes(include=['int64','float64'])

# Apply Min-Max Scaling
scaler=MinMaxScaler()
scaledata=scaler.fit_transform(num_cols)

# Convert back to DataFrame
scaledf=pd.DataFrame(scaledata,columns=num_cols.columns)

print('Rescaled Data:\n')
print(scaledf.head(10))
