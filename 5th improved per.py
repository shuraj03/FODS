import numpy as np
import matplotlib.pyplot as plt
fuel_efficiency = np.array([25, 30, 20, 22, 28])
average_efficiency = np.mean(fuel_efficiency)
model1=fuel_efficiency[1]
model2=fuel_efficiency[3]
pre_imp=((model2-model1)/model1)*100
print("Imoroved precentage:",pre_imp)
