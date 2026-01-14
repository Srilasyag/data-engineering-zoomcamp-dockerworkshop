import sys


print('hello pipeline')


import sys
print("arguments", sys.argv)

month = int(sys.argv[1])
print(f"Running pipeline for month{month}")

import pandas as pd

df = pd.DataFrame({"day": [1, 2], "Bnum_passengers": [3, 4]})
print(df.head())
df['month']=month
print(df.head())
df.to_parquet(f"output_{month}.parquet", index=False)

print(f"hello pipeline, month={month}")