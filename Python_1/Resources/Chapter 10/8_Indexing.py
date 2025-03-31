import numpy as np
ar=np.arange(10).reshape(2,5)
print(ar)

for i in ar:
    for j in i:
        print(j)
#or
for i,d in np.ndenumerate(ar):
    print(i,d)
    