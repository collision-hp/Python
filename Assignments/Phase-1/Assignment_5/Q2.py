dict={}
n=int(input("Enter the number of students"))
for i in range(n):
    name=input("Enter your name")
    marks=int(input("Enter your marks "))
    dict[name]=marks
print(dict)