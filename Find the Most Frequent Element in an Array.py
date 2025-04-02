#Q5. Find the Most Frequent Element in an Array

import numpy as np

arr= [1, 2, 2, 3, 3, 3,33, 4, 4, 4, 4]
values,counts=np.unique(arr,return_counts=True)

most_frequent=values[np.argmax(counts)]
print("Most Frequent Element:", most_frequent)
