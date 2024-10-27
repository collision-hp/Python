day=int(input("Enter the no. of days"))
hrs=int(input("Enter the hours"))
min=int(input("Enter the minutes"))
sec=int(input("Enter the seconds"))

ds=day*24*60*60
hs=hrs*60*60
ms=min*60
ss=sec

print("Total number of seconds",ds+hs+ms+ss)