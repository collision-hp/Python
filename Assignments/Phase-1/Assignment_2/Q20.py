li=[]
n=int(input("Enter an integer"))
for i in range (1,n+1):
    if n%i==0:
        li.append(i)
print(li)