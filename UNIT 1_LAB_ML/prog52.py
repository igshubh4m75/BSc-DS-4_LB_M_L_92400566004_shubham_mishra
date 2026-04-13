import pandas as pd

s = pd.Series(['apple'])
print("====starts with ====")
print(s.str.startswith('a'))
print("====ends with =====")
print(s.str.endswith('e'))
