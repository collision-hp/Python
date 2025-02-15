import re

def count_string_components(s):
    digits = len(re.findall(r'\d', s))
    non_digits = len(re.findall(r'\D', s))
    whitespace_chars = len(re.findall(r'\s', s))
    words = len(re.findall(r'\w+', s))
    
    return digits, non_digits, whitespace_chars, words

s = "Hello World! 1234, let's count 56 words."

digits, non_digits, whitespace_chars, words = count_string_components(s)

print(f"Digits: {digits}")
print(f"Non-digit characters: {non_digits}")
print(f"Whitespace characters: {whitespace_chars}")
print(f"Words: {words}")
