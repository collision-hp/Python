def great(n):
    li=[]
    while(n!=0):
        li.append(n%10)
        n//=10
    li.sort()
    li.reverse()
    li.pop()
    print(li)

n=int(input('Enter a number'))
great(n)