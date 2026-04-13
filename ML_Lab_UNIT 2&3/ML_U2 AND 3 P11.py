# Program11 unit-2
# Encoding Data
import pandas as pd
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv('airlines.csv')
label_enc=LabelEncoder()
# Encode 'origin' column
df['Callsign_encoded']=label_enc.fit_transform(df['Callsign'])
print('Encoded data (Callsign column):\n')
print(df[['Callsign','Callsign_encoded']].head(10))
