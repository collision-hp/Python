str=input("Enter a string ")
l=len(str)
substr=[]
for i in range (0,l):
    for j in range(i+1,l+1):
        substr.append(str[i:j])
print(substr)