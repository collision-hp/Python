import numpy as np
def med_mode(arr):
    median=np.median(arr)
    print(median)
    mode=np.bincount(arr).argmax()
    print(mode)
arr1=np.arange(1,8)
med_mode(arr1)


