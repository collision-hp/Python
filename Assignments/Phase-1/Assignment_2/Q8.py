while(True): 
    n=int(input("Enter a number"))
    if n>0:
        break
if n%2==0:
    n*=2
else:
    n**=2
print(n)
    