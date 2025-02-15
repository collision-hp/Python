x = "madam"
w = ""
for i in x:
    w = i + w
if (x == w):
    print("Yes")
else:
    print("No")
   
   
   
s = "racecar"
def isPalindrome(str):
    for i in range (0,len(str)):
        if str[i]!=str[(len(str)-i-1)]:
            print("Not Palindrome")
    else:
        print("Palindrome")
isPalindrome(s)

