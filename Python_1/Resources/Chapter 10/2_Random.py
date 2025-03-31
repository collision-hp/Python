import numpy as np
#generates random values between 0 to 1
arr1=np.random.rand(6)
print(arr1)
#generates both positive and negative values close to 0
arr2=np.random.randn(5)
print(arr2)
#generates random floats between 0 to 1
arr3=np.random.ranf(6)
print(arr3)
#generates random int values in given range
min=5
max=10
total=8
arr4=np.random.randint(min,max,total)
print(arr4)


