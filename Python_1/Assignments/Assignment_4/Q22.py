numbers=[10,3,7,1,9,4,2,8,5,6]
# list(map(lambda x:x*2,filter(lambda x:x%2==0,numbers)))
li=list(filter(lambda x:x%2==0,map(lambda x:x*2,numbers)))
print(li)
print("Map is applied first so it doubles all the number 1st then lambda expression is evaluated")

