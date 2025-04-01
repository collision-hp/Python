def rotate(a,b,c):
    return (c,a,b)
a,b,c="Doug",22,1974
#unpacking into a,b,c
a,b,c=rotate(a,b,c)
print(a,b,c)
a,b,c=rotate(a,b,c)
print(a,b,c)
a,b,c=rotate(a,b,c)
print(a,b,c)
print()