n=int(input("Enter the length of list"))
li=[]
for i in range(n):
    word=input("Enter the words")
    words=word.lower()
    li.append(words)
s=set(li)
print(s)
            
        
        