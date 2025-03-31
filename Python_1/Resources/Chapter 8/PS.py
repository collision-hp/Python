# #Q1
# def goat(n1,n2,n3):
#     if(n1>n2 and n1>n3):
#         print(f"{n1} is the greatest")
#     elif(n2>n1 and n2>n3):
#         print(f"{n2} is the greatest")
#     elif(n3>n2 and n3>n1):
#         print(f"{n3} is the greatest")
    

# n1=int(input("Enter the 1st number"))
# n2=int(input("Enter the 2nd number"))
# n3=int(input("Enter the 3rd number"))
# goat(n1,n2,n3)

# #Q2
# def convert(cel):
#     far=cel*1.8+32
#     print(f"The farenheit value of {cel} is {far}")

# cel=int(input("Enter the celcius value"))
# convert(cel)

# #Q3
# print("this is a sentence ", end='')
# print("This is the next line")

# #Q4
# def nsum(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     return sum

# n=int(input("Enter a number"))
# print(f"Sum of 1st {n} natural numbers is {nsum(n)}")

# #Q5
# def pattern(n):
#     for i in range(0,n+1):
#         print("*" * (n-i))
        
# n=int(input("Enter a number"))        
# pattern(n)

# #Q6
# def conv(inc):
#     cms=inc*2.54
#     print(cms)
    
# inc=int(input("Enter the number in inches"))
# conv(inc)

# #Q7
# def conlst(list,word):
#     list.remove(word)
#     print(list)
    
# list=["Rohit" , 12 , "Gill" , 99 , "King" , 18]
# option=int(input("Choose an option for removing the element\n 1-Integer Value \n 2-String Value\n"))
# if (option==1):
#     word=int(input("Enter the integer\n"))
# elif (option==2):
#     word=input("Enter the String\n")
    
# conlst(list,word)

#Q8
def mul(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")

n=int(input("Enter a number"))
mul(n)