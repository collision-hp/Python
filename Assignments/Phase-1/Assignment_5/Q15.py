import random
rolls=[random.randrange(1,7) for i in range(100000)]
win={}
lose={}
wins=0
loses=0
print(rolls)
for i in rolls:
    if (i==1 or i==2 or i==3):
        wins+=1
        win[i]=wins
    elif (i==4 or i==5 or i==6):
        loses+=1
        lose[i]=loses
print(win)
print(lose)
winper=(wins/100000)*100
loseper=(loses/100000)*100
print(winper)
print(loseper)




roll=[random.randrange(1,10) for i in range(100)]
print(roll)