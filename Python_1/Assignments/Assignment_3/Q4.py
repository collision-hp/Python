def rstr(str):
    x=""
    for i in range (0,len(str)):
        x=str[i]+x
    print(x)
str=input("Enter a string ")
rstr(str)