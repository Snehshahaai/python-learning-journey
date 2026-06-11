import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("Sum of all elements: ",np.sum(arr))
print("Sum of each Row: ",np.sum(arr,axis=1))
print("Sum of Each Cols: ",np.sum(arr,axis=0))
print('Mean of Each Row: ',np.mean(arr,axis=1))
print('Mean of Each Cols: ',np.mean(arr,axis=0))