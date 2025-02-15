chr=input('''Enter your choice 
            a. Create a list of N integers
            b. Display the list elements
            c. Insert an element at a specific position
            d. Delete an element at a given position
            e. Exit''' )
li=[]
inl=int(input("Enter the number of elements you want to enter"))
match chr:
    case 'a':
        for i in range(inl):
            inp=int(input("Enter the elements"))
            li.append(inp)
    case 'b':
        print(li)
    case 'c':
        n=int(input("Enter the position for insertion"))
        ele=input("Enter the element you want to insert")
        li.append(n,ele)
    case 'd':
        m=int(input("Enter the position for deletion"))
        li.pop(m)
    case 'e':
        print("Thankyou")
        


