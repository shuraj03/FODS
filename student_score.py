import pandas as pd
import numpy as np
data=pd.read_csv("student_score.csv")

avg_data = np.mean(data, axis=0)
print(avg_data)
hig_sub=np.argmax(avg_data)
subject=['math','science','english','history']
print(subject[hig_sub],"=",max(avg_data))
