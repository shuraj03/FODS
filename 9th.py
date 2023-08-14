import pandas as pd
import numpy as np

file= pd.read_csv("9data.csv")

property_data=pd.DataFrame(file)
average_price_by_location = property_data.groupby('location')['price'].mean()
print(average_price_by_location)
pbt=property_data['nb']>4
nopbt=len(pbt)
print("No of properties with more than 4 bedroom:",nopbt)
a_sq=property_data['area'].max()
print("property Which has largest S.sq:",a_sq)
