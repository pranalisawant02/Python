#Q3.Calculate Total Revenue from Products Sold

import numpy as np

quantities = np.array([10, 15, 7, 20])
prices = np.array([50, 40, 100, 30])

total_rev=np.sum(quantities*prices)
print("Total Revenue:", total_rev)
