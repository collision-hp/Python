import numpy as np
ar1=np.array([[1,2,3,4],[6,7,8,9]])
print(ar1.shape)
ar2=np.array([1,2,3,4],ndmin=5)
print(ar2.shape)

x=ar1.reshape(4,2) #no of row and no of elements in each row i.e uniform for all rows

print(x)

y=ar1.reshape(-1)
print(y)