s={1,5,32,54,5,5,5,"Harry"}
print(s,type(s))

s.add(566)
print(s)

l=len(s)
print(l)

s.remove(5)
print(s)
print('''<---x---x---x---x---x--->\n''')
#SET UNION AND INTERSECTION

s1={1,8,5,6}
s2={7,8,5,2}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1-s2)
