s1={'red','green','blue'}
s2={'cyan','green','blue','magenta','red'}
print(s1==s2)
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1>s2)
print(s1<s2)

print(s1.union(s2))
print(s1.intersection(s2))
print(s1-s2)
print(s2-s1)