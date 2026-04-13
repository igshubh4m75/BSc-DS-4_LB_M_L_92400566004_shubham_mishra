# Program5 unit-2
#First Version - converts categories into numbers.
import pandas as pd
from sklearn.preprocessing import LabelEncoder
# Load dataset
ds = pd.read_csv('auto-mpg.csv')
# Create LabelEncoder object
lable_enc = LabelEncoder()
# Encode 'origin' column
ds['origin_encoded'] = lable_enc.fit_transform(ds['origin'])
print('Encoded Data (origin column):\n')
print(ds[['origin', 'origin_encoded']].head(10))
