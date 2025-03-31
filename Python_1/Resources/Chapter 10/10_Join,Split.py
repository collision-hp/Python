import numpy as np
ar1=np.arange(10,18).reshape(2,4)
ar2=np.arange(8).reshape(2,4)
print(ar1)
# ar2=np.random.randint(1,8,8)
print(ar2)
arr=np.concatenate((ar1,ar2),axis=1)
print(arr) #merging column wise
arr=np.concatenate((ar1,ar2),axis=0)
print(arr) #merging row wise

arst=np.stack((ar1,ar2),axis=1)
print(arst)
