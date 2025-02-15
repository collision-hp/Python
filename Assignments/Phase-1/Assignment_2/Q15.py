n=int(input("Enter a number"))
li=[]
for i in range (1,n):
    if n%i==0:
        li.append(i)
sum=sum(li)
print(sum)
if(sum==n):
    print("Pefect number")