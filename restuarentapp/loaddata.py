import sqlite3
import pandas as pd

conn = sqlite3.connect('../db.sqlite3')
df = pd.read_csv('../sam.csv')
df['id'] = df.index
df=df[['id', 'Segment', 'Country', 'Product', 'Units', 'Sales', 'Datesold']]


print(df.columns)

df.to_sql('restuarentapp_productmodel', conn, if_exists='replace', index=False)

