str='mississippi'
dct={}
for i in str:
    count=0
    for j in str:
        if(j==i):
            count+=1
    dct[i]=count
print(dct)