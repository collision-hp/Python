import pandas as pd
l=["Cry","Apple","Orange","Sky","Banana"]
s=pd.Series(l)
vowser=s[s.str.contains('[AEIOUaeiou]',regex=True)]
srtvowser=s[s.str[0].str.match('[AEIOUaeiou]')]
print(vowser)
print(srtvowser)