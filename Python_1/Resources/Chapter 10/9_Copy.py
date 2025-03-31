import numpy as np
arr=np.arange(12).reshape(2,6)

cp=arr.copy()
vw=arr.view()
arr[1]=12

print(arr)
print(cp)#NO CHANGE IN COPY
print(vw)#CHANGE IN VIEW

