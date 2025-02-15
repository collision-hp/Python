roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5}
li=list(i for i in roman_numerals)
print(li)
li2=list(roman_numerals[i] for i in roman_numerals)
print(li2)
li3=list(roman_numerals.items())
print(li3)


