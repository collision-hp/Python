li=[]
licum=[]
for i in range(5):
    i=int(input("Enter 5 elements"))
    li.append(i)
sum=0
for i in li:
    sum+=i
    licum.append(sum)
print(li)
print(licum)