def calc(n,m,op):
    match op:
        case '+':
            return n+m
        case '-':
            return n-m
        case '*':
            return n*m
        case '/':
            return m/n


op=input("Enter the operator")
n=int(input("Enter the 1st integer"))
m=int(input("Enter the 2nd integer"))
print(calc(n,m,op))