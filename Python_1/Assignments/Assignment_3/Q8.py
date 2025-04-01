month=input("Enter the month")
li31=["January","March","May","July","August","October","December"]
li30=["April","June","September","November"]
def days():
    if month in li31:
        print("31")
    elif month in li30:
        print("30")
    else:
        print("28/29")
days()