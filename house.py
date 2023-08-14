import pandas as pd
import numpy as np
file=pd.read_csv("house_data.csv")


price=file["price"]
bedroom=file["bedroom"]
avg_4bedroom= np.mean(price[bedroom>3])
print("avg of 4 bedroom =",avg_4bedroom)
