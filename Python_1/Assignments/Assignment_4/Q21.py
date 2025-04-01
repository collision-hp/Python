numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers)))
print("The filter lambda is called 10 times")
print("5 times for 3 7 1 9 5")

list(filter(lambda x: x % 2 != 0, map(lambda x: x ** 2, numbers)))
print("The map lambda will be called 10 times ")
