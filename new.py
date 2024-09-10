import pandas as pd
new=pd.read_csv('cereal.csv')
print(new)


missing=new.isna().any()
missings=new.isnull().sum()
print(missing)
print(missings)

row=slice(0,9)
c