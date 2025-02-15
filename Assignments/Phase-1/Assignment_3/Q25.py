def coprime(n,m):
    li1=[]
    li2=[]
    for i in range(2,n):
        if n%i==0:
            li1.append(i)
    for j in range(2,m):
        if m%i==0:
            li2.append(j)
    for i in li1:
        for j in li2:
            if i==j:
                print("Not Coprime")
                break    
        else:
            print("Coprime")
        break
coprime(15,8)