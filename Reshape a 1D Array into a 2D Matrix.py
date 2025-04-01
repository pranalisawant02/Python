 #Q2.Reshape a 1D Array into a 2D Matrix

import numpy as np

sales_data=np.array([1000, 1200, 1500,1800, 2000, 2100, 2500, 2700])
sales_matrix=sales_data.reshape(4,2)
print(sales_matrix)
