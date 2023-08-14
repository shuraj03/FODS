import matplotlib.pyplot as plt
import pandas as pd

file= pd.read_csv("11th data.csv")
a= pd.DataFrame(file)

month = a['month']
sale = a['sale']

plt.plot(month,sale)
plt.show()
plt.bar(month,sale)
plt.show()
plt.scatter(month,sale)
plt.show()

