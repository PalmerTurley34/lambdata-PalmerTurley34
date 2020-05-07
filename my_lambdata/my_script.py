import pandas as pd 
from my_lambdata.my_mod import date_cols
from my_lambdata.my_mod2 import list_to_col

df = pd.DataFrame({'num': [1,2,3], 'date':['2016-05-09', '2020-05-06', '1993-12-25']})
print(df)

date_cols(df, 'date')
print(df)

colors = ['red', 'yellow', 'blue']
list_to_col(df, colors, 'Colors')
print(df)