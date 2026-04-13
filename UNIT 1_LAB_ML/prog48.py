import pandas as pd
s1 = pd.Series(["   Hello   Hello    G"])
print(s1.str.strip())
