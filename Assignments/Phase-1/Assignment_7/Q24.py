str="uuhggggdd"
freq={}
for i in str:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
max=0
for i in freq.values():
    if i>max:
        max=i
print(max)

for key,val in freq.items():
    if val==max:
        print(key)
        
#OR

ll=list(str)   
max=1  
chr=''
for i in ll:
    cc=ll.count(i)
    if cc>max:
        max=cc
        chr=i
print(max)
print(chr)
