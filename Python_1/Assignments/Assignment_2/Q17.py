eles=0
for i in range (100,1000):
    if i%5==0 or i%6==0 :
        print(i," ",end='')
        eles+=1
        if eles%10==0:
            print()