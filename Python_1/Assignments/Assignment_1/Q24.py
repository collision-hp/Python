a=int(input("Enter 1st integer"))
b=int(input("Enter 2nd integer"))
c=int(input("Enter 3rd integer"))

m=max(a,b,c)
n=min(a,b,c)
mid=(a+b+c)-m-n

print('Sum',m+n+mid)