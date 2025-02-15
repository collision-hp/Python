str="Write a bcriptd that reads a line of text"
ls=str.split(" ")
for i in ls:
    if i.startswith("b") and i.endswith("d"):
        print(i)
    