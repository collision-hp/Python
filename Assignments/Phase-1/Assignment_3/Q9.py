lb=[]
def convertdb(n):
    i=0
    while(n>0):
        i=n%2
        lb.append(i)
        n//=2
    lb.reverse()
    print(lb)
convertdb(21)

def convertbd(n):
    d=0
    for i in range (0,len(str(n))):
        d+=(n%10)*(2**i)
        n//=10
    print(d)
convertbd(110)