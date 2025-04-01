li=[12,34,32,18,12,43,12]
n=int(input("Enter the element you want to delete"))
while n in li:
    li.remove(n)
print(li)