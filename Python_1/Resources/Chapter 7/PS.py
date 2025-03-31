# #Q1
# num=int(input("Enter a number\n"))

# for i in range(1,11):
#     print(f"{num} * {i} = {num*i}") #f string is used to print variables in string form
# #Q3    
# i=1
# while(i<11):
#     print(f"{num}*{i}={num*i}")  
#     i+=1  
    
# #Q2
# l={"Harry","Chin-Chin","Sreyas","Sahul"}
# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")
        
# #Q4
# num=int(input("Enter a number\n"))
# for i in range(2 , num):
#     if((num%i)==0):
#         print("Not Prime")
#         break
# else:
#     print("Prime")           


# #Q5
# n=int(input("Enter a number\n"))
# i=1
# sum=0
# while(i<n+1):
#     sum+=i
#     i+=1
# print(sum)
    
# #Q6
# n=int(input("Enter a number\n"))
# fact=1
# for i in range(1, n+1):
#     fact=fact*i

# print(f"The factorial of {n} is {fact}")

# #Q7
# '''  
#   *
#  ***
# *****
# '''
# n=int(input("Enter a number\n"))
# for i in range(1,n+1):
#     print(" " * (n-i), end="") #printing space ,,, print statement gives us a new line by default if we'll write end then it'll print on the same line
#     print("*" * (2*i-1), end="") #printing star
#     print("") #for a new line

# #Q8
# '''  
# *
# **
# ***
# '''
# n=int(input("Enter a number\n"))
# for i in range(1,n+1):
#     print("*" * (i) ,end="")
#     print("")
    
# #Q9
# '''
# ***
# * *
# ***
# '''
# n=int(input("Enter a number\n"))
# for i in range(1,i+1):
#     if(i==1 or i==n):
#         print("*" *n , end="")
#     else:
#         print("*" , end="")
#         print(" " * (n-2), end="")
#         print("*" , end="")
#     print("")

# #Q10
# n=int(input("Enter a number \n"))
# for i in range(1,11):
#     print(f"{n}X{i}={n*i}")

'''
1 10  }
2 9    }
3 8     }
4 7      }
5 6       }  sum = 11 ; So 11 - i for reverse in place of i
6 5      }
7 4     }
8 3    }
9 2   }
10 1 }
'''    
n=int(input("Enter a number \n"))
for i in range(1,11):
    print(f"{n}X{11-i}={n*(11-i)}")