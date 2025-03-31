import numpy as np
arr=np.array([3,6,3,1])
print(arr)

x=[1,2,3,4]
y=np.array(x)
print(y)
print(type(y))
print(y.ndim)

# li=[]
# for i in range(1,5):
#     n=int(input("Enter the numbers"))
#     li.append(n)
# x=np.array(li)
# print(x)

ar2=np.array([[1,2,3,4],[6,7,8,9]])
print(ar2)
print(ar2.ndim)
print(ar2.shape)

ar3=np.array([1,2,3,4],ndmin=8)
print(ar3)
