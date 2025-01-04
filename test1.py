# Sales Data
sales_data = {
    "Month": ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"],
    "Sales": [5000, 7000, 8000, 6000, 9000, 11000, 9500, 12000, 10500, 8000, 7500, 6000]
}

import pandas as pd
import matplotlib.pyplot as plt
df1=pd.DataFrame(sales_data)
df2=pd.DataFrame(grades_data)
plt.bar(df1['Month'],df1['Sales'])
plt.title("cOMPANY sALES")
plt.xlabel('Months')
plt.ylabel('Sales')
plt.show()