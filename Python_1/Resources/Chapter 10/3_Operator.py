import numpy as np
#addition/subtraction/multiplication/division of specific value to whole array
ar1=np.array([1,2,3,4])
adadd=ar1+61
print(adadd)

#addition/subrtaction of 2 array
ar2=np.array([5,6,7,8])
mul=ar1*ar2
print(mul)

#operations using function
add=np.add(ar1,ar2)
print(add)
div=np.divide(ar1,ar2)
print(div)
multi=np.multiply(ar1,ar2)
print(multi)
mod=np.mod(ar2,ar1)
print(mod)
reci=np.reciprocal(ar1)
print(reci)
pow=np.pow(ar1,2)
print(pow)
#2D array operations
arr1=np.array([[1,2,3,4],[5,6,7,8]])
arr2=np.array([[5,6,7,8],[1,2,3,4]])
add=arr1+arr2
print(add)

adar=np.multiply(arr1,arr2)
print(adar)

