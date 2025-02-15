import numpy as np
ar1=np.array([[0,1],[2,3]])
ar2=np.array([[4,5],[6,7]])
ar3=np.stack((ar1,ar2))
ar4=np.hstack((ar1,ar2))
ar5=np.vstack((ar4,ar4))
ar6=np.hstack((ar3,ar3))
print(ar3)
print(ar4)
print(ar5)
print(ar6)




