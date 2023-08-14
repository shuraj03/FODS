import matplotlib.pyplot as plt
import pandas as pd

file= pd.read_csv("11th data.csv")
a= pd.DataFrame(file)

month = a['month']
sale = a['sale']


#line
plt.figure(figsize=(15,15))
plt.plot(month, sale, marker='o', linestyle='--', color='b')
plt.title('Monthly Sales Prediction')
plt.xlabel('month')
plt.ylabel('sale')
plt.grid(True)
plt.show()


#bar
plt.figure(figsize=(10, 6))
plt.bar(month, sale, color='g')
plt.title('Monthly Sales Data')
plt.xlabel('month')
plt.ylabel('sale')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()



#scatter
plt.figure(figsize=(10, 6))
plt.scatter(month, sale, color='r', marker='o')
plt.title('Monthly Sales Prediction')
plt.xlabel('month')
plt.ylabel('sale')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
