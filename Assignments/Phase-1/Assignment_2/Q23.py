wd=int(input("Enter the amount you want to withdraw"))

if wd%10!=0:
    print("Enter a valid withdrawl amount a multiple of 10")

sum100=0
sum50=0
sum20=0
sum10=0
while (wd!=0):
    if wd>=100:
        sum100=wd//100
        wd-=sum100*100
    elif wd>=50:
        sum50=wd//50
        wd-=sum50*50
    elif wd>=20:
        sum20=wd//20
        wd-=sum20*20
    elif wd>=10:
        sum10=wd//10
        wd-=sum10*10
    

print(sum100)
print(sum50)
print(sum20)
print(sum10)
