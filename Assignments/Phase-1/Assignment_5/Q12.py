set=input("Enter a sentence")
word=set.lower().split()
words={}
for i in word:
    if i in words:
        words[i]+=1
    else:
        words[i]=1
# print(words)

dup={i:count for i ,count in words.items() if count>1}
print(dup)
print(len(dup))