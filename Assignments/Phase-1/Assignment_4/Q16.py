li=[]
n=int(input("Enter the number of elements"))
li.append(n)
for _ in range(n):
    ele=int(input("Enter the element"))
    li.append(ele)

if li==sorted(li):
    print("Yes")
else:
    print("No")
