str="consonants"
cvol=0
ccon=0
for i in  str:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        cvol+=1
    else:
        ccon+=1
print(f"No. of consonant {ccon} , Number of vowels {cvol}")