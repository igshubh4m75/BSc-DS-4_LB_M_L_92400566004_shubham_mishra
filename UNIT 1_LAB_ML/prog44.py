import pandas as pd
df = pd.DataFrame({'A':[1,2,3]})
print("===cumulative sum====")
print(df.cumsum())
print("===cumulative product====")
print(df.cumprod())
