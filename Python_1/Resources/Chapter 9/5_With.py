f=open("file.txt")
print(f.read())
f.close()

#the same can be written like this
with open("file.txt") as f:
    print(f.read())

#you don't have to open and close the file explicitely