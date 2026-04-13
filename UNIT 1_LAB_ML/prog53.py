import pandas as pd

s = pd.Series(['papple'])
print("====find ====")
print(s.str.find('p'))
print("====findall =====")
print(s.str.findall('p'))
