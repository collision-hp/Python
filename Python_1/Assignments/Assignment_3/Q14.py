def arm(n):
    sum=0
    m=int(n)
    while(m>0):
        digit=m%10
        sum+=digit**len(n)
        m//=10

    if int(n)==sum:
        print("Arm")
    else:
        print("Not Arm")
        
n=input("Enter a number")
arm(n)