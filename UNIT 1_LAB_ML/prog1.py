import pandas as pd
from io import StringIO

csv_data = '''A, B, C, D
            1, 2, 3, 4
            5, 6, , 8
            9, 10, 11, '''

df = pd.DataFrame(StringIO(csv_data))
print("Data Frame Print")
print(df)

print("Dataframe columns with will Sum")
print(df.isnull().sum())