import numpy as np
arr=np.array([2**i for i in range(0,6)]).reshape(2,3)

print(arr)
ar1=arr.flatten()
print(ar1)
ar2=arr.ravel()
print(ar2)
