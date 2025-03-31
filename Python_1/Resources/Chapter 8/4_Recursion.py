'''
factorial(1)=1
factorial(2)=2X1
factorial(3)=3X2X1
factorial(4)=4X3X2X1
factorial(5)=5X4X3X2X1

factorial(n)=nx(n-1)x(n-2)x......3x2x1

factorial=(n)x(n-1)!
'''
def fact(n):
    if (n==1):
        return 1
    return n*fact(n-1)
n=int(input("Enter a number"))
print(f"The factorial of {n} is {fact(n)}")