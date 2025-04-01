import math
n=int(input("Enter the number of terms you want to find the sum of"))
x=int(input("Enter the value of x"))
sum1=1
sum2=1
sum3=1
sign=-1
for i in range (1,n+1):
    term1=(x**(2*i))/math.factorial(2*i)
    sum1+=sign*term1
    sign*=-1
print(sum1)
for i in range (1,n+1):
    term2=(x**i)/math.factorial(i)
    sum2+=term2
print(sum2)
for i in range (1,n+1):
    term3=2*i+1
    sum3+=sign*term3
    sign*=-1
print(sum3)
