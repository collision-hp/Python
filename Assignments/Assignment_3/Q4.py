str=input("Enter a string")
li=[]
l=len(str)
def rstr():
    for i in range (l):
        li.append(str[i])
    li.reverse()
    print(li)
rstr()