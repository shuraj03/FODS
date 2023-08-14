import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature_values = [10, 12, 15, 20, 25, 28, 30, 29, 26, 22, 18, 12]
rainfall_values = [50, 40, 30, 20, 10, 5, 3, 5, 10, 20, 30, 40]


plt.plot(months, temperature_values)
plt.show()




plt.scatter(months, rainfall_values)
plt.show()
