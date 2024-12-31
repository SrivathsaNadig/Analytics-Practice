import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('textbookdata.csv')
import numpy as np
print(df.columns)

print(df.head(5))
print(df.shape)
print(df.describe())
print(df.isnull().sum())
print(df[df['Region']=='North'])
print(df.groupby('Product')['Quantity'].sum())
print(df.groupby('Region')['Total Sales'].mean())
print(df['Quantity'].corr(df['Total Sales']))
df['Profit']=df['Total Sales']-(df['Quantity']*df['Price'])
df.to_csv('sales_data_with_profit.csv')

correlation = np.corrcoef(df['Quantity'], df['Total Sales'])[0, 1]
print(f'Correlation between Quantity and Total Sales: {correlation:.2f}')

pivot_table = df.pivot_table(values='Total Sales', index='Product', columns='Region', aggfunc='sum', fill_value=0)
print("Pivot Table of Total Sales for Each Product in Each Region:")
print(pivot_table)