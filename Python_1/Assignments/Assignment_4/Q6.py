li=[]
for i in range(10):
    i=int(input("Enter 10 elements"))
    li.append(i)
search=int(input("Enter the number to search"))

if search in li:
    tot=li.count(search)
print(tot)