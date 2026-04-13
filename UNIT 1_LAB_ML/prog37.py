import pandas as pd

df = pd.DataFrame({'A':[1,2,3,None],'B':[4,5,6,7]})
print(df.T)
