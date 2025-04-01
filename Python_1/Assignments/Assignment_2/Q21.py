n=int(input("Enter an integer"))
fact=1
for i in range(1,n):
    fact*=i
    if fact==n:
        print("Yes n is a factorial number")
        break    
else:
    print("No n is not a factorial number")
    