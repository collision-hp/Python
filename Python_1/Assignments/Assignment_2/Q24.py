'''Process - 1'''
n=int(input("Enter an integer"))
digit={0:'ZERO',1:'ONE',2:'TWO',3:'THREE',4:'FOUR',
       5:'FIVE',6:'SIX',7:'SEVEN',8:'EIGHT',9:'NINE'}
numdigit=[]

while(n>0):
    numdigit.append(n%10)
    n//=10
numdigit.reverse() #since we started collecting the digits from the last element
for value in numdigit:
    print(digit[value] ," ",end='')
    
