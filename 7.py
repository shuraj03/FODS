import pandas as pd
data={
'c_id':[1,2,3,3,5],
'order_date':[12,14,22,20,30],
'p_name':["watch","tv","phone","stand","charger"],
'order_quantity':[2,1 ,1,3,4]
}
y=pd.DataFrame(data)
a = y.groupby('c_id')['order_quantity'].sum()
print("The total number of orders made by each customer:", a)
q=min(data['order_date'])
m=max(data['order_date'])
print("The earliest order dates in the dataset:", q)
print("The latest order dates in the dataset:",m)
