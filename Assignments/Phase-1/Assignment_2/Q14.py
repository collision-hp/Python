dict={'Standard':100,
      'Deluxe':150,
      'Suite':250}
room=input(f"Enter your room type {dict}")
value=dict.get(room)
# print(value)
nights=int(input("Length of stay"))
if(nights>3 and nights<7):
    disc=value*10/100
elif(nights>7):
    disc=value*20/100
value-=disc
season=input("Enter the season\nA-Peak Season\nB-Off-Season")
if(season=='A'):
    value+=value*20/100
elif(season=='B'):
    value-=value*15/100
    
mbrship=input("Are you a loyalty member- Yes or No")
if mbrship=='Yes':
    value-=value*5/100
    print(f"Your 5% additional discount will be applied")
else:
    print("No discount")
print("Final booking cost is ",value)