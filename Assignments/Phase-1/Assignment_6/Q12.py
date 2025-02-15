import numpy as np
ar1=np.array([[0,1],[2,3]])
ar2=np.array([[4,5],[6,7]])
ar3=np.concatenate((ar1,ar2),axis=1)#row
ar4=np.concatenate((ar1,ar2),axis=0)#column
print(ar3)
print(ar4)

