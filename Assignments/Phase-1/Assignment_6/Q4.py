import numpy as np
arr=np.random.randint(0,20,(2,2))
print(arr)

arr[[0,1]]=arr[[1,0]]
arr[:,[0,1]]=arr[:,[1,0]]
print(arr)
