dict={}
ni=int(input("Enter the number of elements"))
for i in range(ni):
    name=input("Enter your name")
    n=int(input("Enter your jersey number"))
    dict[name]=n
print(sum(dict.values()))
