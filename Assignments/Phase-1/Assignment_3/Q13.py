def rtn(roman):
    def value(char):
        match char:
            case 'I':
                return 1
            case 'V':
                return 5
            case 'X':
                return 10
            case _:
                return "Error"
    ineq = 0
    for i in range (len(roman)):
        if value(roman[i]) > value(roman[i-1]):
            ineq = value(roman[i])-value(roman[i-1])
        else:
            ineq = value(roman[i])+value(roman[i-1])
    
    return ineq
roman = input("Enter a Roman numeral: ")
print(f"The integer value of {roman} is: {rtn(roman)}")
