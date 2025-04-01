import random
li=[]
n=int(input("Enter the number of digits you want to get"))
for i in range (10):
    value=random.randrange(1,100)
    li.append(value)
print(f"Sum is {sum(li)} and average is {sum(li)/n} ")
