import pandas as pd
s1=pd.Series([1,1,3,7,88,12,88,23,3,1,9,0])
min=s1.idxmin()
max=s1.idxmax()
print(f"Smallest number index is {min} and largest number index is {max}")
