import numpy as np
sales_data=np.array([50, 60, 70, 80])
sales_dat=np.sum(sales_data)
print("total sum fo the year=",sales_dat)
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100
print("avg of 4th quat=",percentage_increase)
