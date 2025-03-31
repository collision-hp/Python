friends=["apple" , "rohit" , "Virat" , 342.98 , 3 , False]

friends.append(8)
friends[1]="Dhawan"
friends.append("Jack") #List is mutable
print(friends)

l1=[1,23,43,8,74,8]
l1.sort()
print(l1)

l2=[12,46,8,3,2,53]
l2.reverse()
print(l2)

l3=[10,53,7,34,4]
l3.insert(3,8) #(index,number)
print(l3)

l4=[3,8,43,2,43,76,43]
cnt=l4.count(43)
print(cnt)

l4.remove(43) #input-the element
print(l4)

l5=[23,4,12,67,8]
l5.pop() #input-index address of element
print(l5) 

print(l5.pop(2)) #this will return the value of the index poped

