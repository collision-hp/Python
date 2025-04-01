mark=int(input("Mark"))
mrks=int(mark/10)
print(mrks)
if mrks>=9:
    print("A-Excelent")
elif mrks==8:
    print("B-Good")
elif mrks==7:
    print("C-Average")
elif mrks==6:
    print("D-Needs Improvement")
elif mrks<6:
    print("F-Fail")
    
    