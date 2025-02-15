dict={}
li=[]
name=input("Enter your name")
n=int(input("Enter number of subjects"))
for i in range(n):
    marks=int(input("Enter your marks"))
    li.append(marks)
dict[name]=li
# print(dict)
en=input("Enter your name to access mark")
print(dict[en])