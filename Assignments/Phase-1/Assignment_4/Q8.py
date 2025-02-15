n=int(input("Enter an integer"))
li=[]
def mullist(n):
    for i in range(1,n+1):
        mul=[i*j for j in range(1,6)]
        li.append(mul)
mullist(n)
print(li)