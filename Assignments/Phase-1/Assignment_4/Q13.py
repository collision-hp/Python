def sorttup(list):
    return sorted(list,key=lambda x:x[1])
list = [(1, 3), (4, 1), (5, 2), (2, 5)]
print(sorttup(list))