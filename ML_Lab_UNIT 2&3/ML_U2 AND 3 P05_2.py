# Program5 unit-2
#Second Version - This is creates separate columns for each category
import pandas as pd
# Load dataset
df = pd.read_csv('auto-mpg.csv')
# Apply One-Hot Encoding on 'origin'
df_encoded = pd.get_dummies(df, columns=['origin'])
print('One-Hot Encoded Data:\n')
print(df_encoded.head())
