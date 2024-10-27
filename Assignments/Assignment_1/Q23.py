n=int(input("Enter a 4 digit number"))
last=n%10
slast=(n%100)/10
snd=(n/100)%10
fst=n/1000
print(int(last))
print(int(slast))
print(int(snd))
print(int(fst))

print('Sum -> ',format(int(last+slast+snd+fst)))