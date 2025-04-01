def prod(n):
    m=1
    while n:
        x=n%10
        m*=x
        n//=10
    print(m)
prod(1234)