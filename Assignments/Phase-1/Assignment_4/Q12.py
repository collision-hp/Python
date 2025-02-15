sum=0
li=[]
for i in range(3):
    inp=[]
    for _ in range(4):
        p=int(input("Enter")) 
        inp.append(p)
    li.append(inp)
print(li)

for i in li:
    for j in i:
        print(j,' ',end='')
    print()
    
for i in range(4):
    total=0
    for j in li:
        total+=j[i]
    print(total)
