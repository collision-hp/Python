a=int(input("Your age"))

#Independent if statement
if(a%2==0):
    print('A is even')
#End of program

#If statement no. 2    
if(a>=18):
    print("You are above the age of concent") #The space before print is called 'Indent' which denotes the statement is inside if condition
    print("Good for you")
    
elif(a<0):
    print("You are entering a wrong age")    
    
elif(a==0):
    print("You are entering a wrong age")    

else:
    print("You are below the age of concent")   
    
print('End of program')    