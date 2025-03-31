# 3 type of strings representation
name='KingKohli'
# name2="king"
# name3='''king'''

nameshort = name[0:4] # start form index 0 and goes till 3(excluding 3)
print(nameshort)

character4=name[4]
print(character4)

length = len(name)
print(length)


print(f"{name:<20}{length}")
print(f"{nameshort:<20}{character4}")
