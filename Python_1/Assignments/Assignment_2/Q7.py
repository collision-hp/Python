n=int(input("Enter an integer"))
pr=[]
for i in range(2,n): 
    for j in range(2,i):
        if i%j==0: 
            break
    else:
        pr.append(i)
print(pr)
print(sum(pr))