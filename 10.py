import matplotlib.pyplot as plt
import pandas as pd
data={'year':[2012,2013,2014,2020,2021],
      'sales':[2000,3000,4000,5000,6000]}
mon=pd.DataFrame(data)
mon.plot.line(x='year',y='sales')
plt.show()
print(mon)
