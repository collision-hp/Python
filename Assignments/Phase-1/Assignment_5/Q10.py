vowel="Synchronization"
dict={}
for i in vowel:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        dict[i]=vowel.count(i)
print(dict)