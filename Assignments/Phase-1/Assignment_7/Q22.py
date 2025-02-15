str="racecar"
ss=str.replace(" ","").lower()
es=str[::-1]
if ss==es:
    print("Symmetric")
else:
    print("Asymmetric")
    
rts=""    
for i in str:
    rts=i+rts

if rts==str:
    print("Symmetric")
    