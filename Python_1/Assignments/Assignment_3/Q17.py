str= input("Enter a string ")
vowels = "aeiouAEIOU"  
upstr=""
for char in str:
    if char not in vowels:
        upstr += char
print(upstr)


str=input("Enter a string")
newstr=""
for i in range(len(str)):
    if (str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u'):
        newstr+=str.replace(str[i],'')
print(newstr) 