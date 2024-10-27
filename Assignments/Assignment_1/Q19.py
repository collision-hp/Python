meal=float(input("Enter the cost of the meal"))
tax=int(input("Enter the tax percentage"))
tip=(18*meal)/100
taxamount=(tax*meal)/100
print("Tax Amount-",taxamount)
print("Tip amount-",tip)
print("Grand total-",meal+tip+taxamount)