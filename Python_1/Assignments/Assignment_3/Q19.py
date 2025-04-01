def gcd(n,m):
    while m:
        temp=m
        m=n%m
        n=temp
    return n
m=int(input("Enter"))
n=int(input("Enter"))
print(gcd(32,60))



