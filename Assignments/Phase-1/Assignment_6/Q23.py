import pandas as pd
data={'Maxine':[32,43,53],'James':[34,23,32],'Amanda':[23,12,42]}
df=pd.DataFrame(data,index=["Morning","Afternoon","Evening"])
print(df)