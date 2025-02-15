def anagram(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()        

    return sorted(str1)==sorted(str2)

str1=input("Enter the 1st string")
str2=input("Enter the 2nd string")
print(anagram(str1,str2))


