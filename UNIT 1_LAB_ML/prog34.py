import pandas as pd

df = pd.DataFrame({'A':[1,2,3,4,5]})
print("========head=========")
print(df.head(3))
print("========tail=========")
print(df.tail(2))
