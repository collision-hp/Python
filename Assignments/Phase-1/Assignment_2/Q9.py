n=input("Enter a number")
if not n.isdigit():
    print("Invalid Input")
else:
    num=int(n)
    rem=num%5
    match rem:
        case 0:
            print("Remainder is 0") 
        case 1:
            print("Remainder is 1")  
        case 2:
            print("Remainder is 2")
        case 3:
            print("Remainder is 3")
        case 4:
            print("Remainder is 4")
