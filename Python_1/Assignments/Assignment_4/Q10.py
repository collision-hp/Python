tup=((23,42,"ijbih",9),(24,12,98.54))
sum=0
for n in tup:
    for ele in n:
        if isinstance(ele,(int,float)):
            sum+=ele
print(sum)
            