li=[(1,2,3,4),(3,2,1),(2,3,1,3),(4,3),(2)]
k=int(input("Enter the length of k"))
li=[i for i in li if isinstance(i,(tuple,list)) if len(i)!=k]
print(li)

