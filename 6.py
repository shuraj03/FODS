import numpy as np
item_price=np.array([100,50,60,70])
quantities=([2,4,3,6])
discount_rate=0.1
tax_rate=0.75
total_cost=(item_price*quantities)
after_discount=(total_cost*discount_rate)
after_tax=(total_cost*tax_rate)
total_cost_after_this=( total_cost-after_discount+after_tax)
print("the total cost of items is:",total_cost)
print("the total cost after discount is:",after_discount)
print("the total cost after tax is:",after_tax)
print("the total cost is:",total_cost_after_this)
