import pandas as pd

s1 = pd.Series(["hello"])
print(s1.str.islower())

s2 = pd.Series(['HELLO'])
print(s2.str.isupper())

s3 = pd.Series(["123"])
print(s3.str.isnumeric())
