import numpy as np
arr=np.random.randint(0,100,(5,5))
print(arr)
count=np.bincount(arr.flatten())
print(count)
