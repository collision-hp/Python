day, high_temperature = ('Monday', 87, 65)
print(day,high_temperature)
#Error extra unpacking values less variables

numbers = [1, 2, 3, 4, 5]
numbers[10]
#index out of bound

name = 'amanda'
name[0] = 'A'
#string immutable

numbers = [1, 2, 3, 4, 5]
numbers[3.4]
#invalid index

student_tuple = ('Amanda', 'Blue', [98, 75, 87])
student_tuple[0] = 'Ariana'
#tuple immutable

('Monday', 87, 65) + 'Tuesday'
#invalid tuple addition

'A' += ('B', 'C') #Invalid addition in tuple

x = 7
del x #del deleetes the variable itself instead of its value 
print(x)

numbers = [1, 2, 3, 4, 5]
print(numbers.index(10))
#index out of bound

numbers = [1, 2, 3, 4, 5]
numbers.extend(6, 7, 8)
#'int' objects are not iterable
#used to add all elements of an iterable list, tuple, or set to the end of a list.

numbers = [1, 2, 3, 4, 5]
numbers.remove(10)
#no 10

values = []
values.pop()
#no elements