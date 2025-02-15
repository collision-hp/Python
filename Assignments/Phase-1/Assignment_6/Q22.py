import pandas as pd
s1=pd.Series([7,11,13,17])
print(s1)

s1=pd.Series([100.0]*5)
print(s1)

import numpy as np
s=pd.Series(np.random.randint(0,101,20))
print(s)

temp=pd.Series([98.6,98.0,100.2,97.9],index=['Julie','Charlie','Sam','Andrea'])
print(temp)

names=['Julie','Charlie','Sam','Andrea']
values=[98.6,98.0,100.2,97.9]
dict=dict(zip(names,values))
ser=pd.Series(dict)
print(ser)

