import numpy as np
ar=np.arange(15).reshape(3,5)
print(ar)
print()
arr1=ar[1]
print(arr1)

print(arr1[:4])#slicing to print values from 5 to 8

print(ar[1][1:3])