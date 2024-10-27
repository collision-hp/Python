wd=int(input("Enter the amount you want to withdraw"))
bal={
    100:10,
    50:50,
    20:40,
    10:100
}
if wd%10!=0:
    print("Enter a valid withdrawl amount i.e a multiple of 10")
total=0
for i in bal:
    balavail=bal.keys(i)*bal.values(i)
    total+=balavail
print(total)
if wd>bal:
    print("ATM doesn't have so much cash available")
