s="how now brown cow"
print(s[s.find('o'):s.rfind('o')])

print(chr(ord('A')+4) + chr(ord('X')+2))

# s = "abc123def456ghi789"
# indices = [i for i, c in enumerate(s) if c == '']
# result = s[indices[1]+1:indices[2]] + s[indices[4]+1:]
# print(result)
# #list index out of range

s = "abracadabra"
print(s.replace(s[s.find('a'):s.find('r')], 'XYZ'))

s = "hello"
shift = 2
print("".join(chr((ord(c) - 97 + shift) % 26 + 97) for c in s))

s = "mississippi"
print("".join(sorted(set(s))))
