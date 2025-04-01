li=[]
def sqev():
    for i in range(1,51):
        if (i%2==0):
            li.append(i**2)
    print(sum(li))
sqev()
            