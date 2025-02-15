str=input("Enter s string")
li=[]
for i in str:
    li.append(i)
s=sorted(set(li))
print(s)