def fact(n):
    facts=1
    while n:
        facts*=n
        n-=1
    print(facts)
fact(5)