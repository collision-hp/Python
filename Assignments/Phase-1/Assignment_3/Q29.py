li=[]
def perf(n):
    for i in range(1,n):
        if n%i==0:
            li.append(i)
    s=sum(li)
    if s==n:
        print("Perfect number")
    else:
        print("Not perfect")
perf(61)