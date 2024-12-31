import pandas as pd
import numpy as np

df=pd.read_csv('SalesCheck2.csv')

print(df.columns)

#Missing Values
missing_values=df.isnull().sum()
print('Missing Value list count is as follows \n',missing_values)

df['Quantity Sold'].fillna(df['Quantity Sold'].mean(),inplace=True)
