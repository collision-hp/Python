str="position"
str1=""
n=len(str)//2
for i in str[:n]:
    str1=i+str1
print(str1+str[n:])