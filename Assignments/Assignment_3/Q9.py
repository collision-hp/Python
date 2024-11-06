l=[]
def convertdb(n):
    i=0
    w=0
    while(n>0):
        i=n%2
        l.append(i)
        n//=2
    l.reverse()
    print(l)
convertdb(312)

def convertbd(n):
    i=0
    w=0
    while(n>0):
        i=n*2
        l.append(i)
        n//=2
    print(l)
convertdb(000111001)
