import pandas as pd

s1 = pd.Series(["HELLO"])
print(s1.str.lower())

s2 = pd.Series(['hello'])
print(s2.str.upper())

s3 = pd.Series(['Hello'])
print(s3.str.swapcase())
