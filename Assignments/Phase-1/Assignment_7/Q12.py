import itertools

str="bathe"
permutations=itertools.permutations(str,3)
for i in permutations:
    print("".join(i))
