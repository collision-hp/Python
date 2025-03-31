marks={
    "Virat":18,
    "Rohit":43,
    "Gill":98,
    "Bumrah":0,
    0:"Keith"
}
print(marks.items()) #whole pair
print(marks.keys()) #key elements
print(marks.values()) # their values

marks.update({"Gill":89}) #updates the marks of gill
print(marks)

marks.update({0:"Junior"}) # updates the string part
print(marks)

marks.update({"Hardik":76}) # adds new pairs like append
print(marks)

print(marks.get("Rohit")) #prints none
print(marks["Rohit"]) #prints error


marks.pop("Rohit") #requires argument
print(marks)

# print(marks.pop("Rohit")) #prints marks of Rohit

#POP Method follows LIFO 
marks.popitem() #doesn't require any argument
print(marks)

print(marks.popitem()) #prints the last element to be popped