import numpy as np
arr=np.array([1,2,3,4,5])
#argmin used to find the position of the min element
print("min",np.min(arr),np.argmin(arr))
print("max",np.max(arr),np.argmax(arr))
print("sqrt",np.sqrt(arr))
print("square",np.square(arr))
print("cumsum",np.cumsum(arr)) #like fibonacci

arr2=np.array([[1,2,3,4],[6,7,8,9]])
#axis=1 -> column , axis=0 -> row
print(np.min(arr2,axis=1),np.argmin(arr2,axis=1))
print(np.max(arr2,axis=0))
print("Transpose\n",arr2.T)





