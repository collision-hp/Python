l1=[10, 20, 30]
l2=[5, 10, 15, 20]
ss=set()
def analyze_sets(l1,l2):
    s1=set(l1)
    s2=set(l2)
    sd=s1.symmetric_difference(s2)
    print(sd)
    for i in sd:
        if (i%2==0):
            i*=2
            ss.add(i)
        else:
            i+=5
            ss.add(i)
    print(ss)
analyze_sets(l1,l2)