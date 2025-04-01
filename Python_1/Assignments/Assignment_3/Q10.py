def uqper(s):
    if len(s) == 0:
        return []
    perm=[]
    for i in range(len(s)):
        char = s[i]
        remaining_str = s[:i] + s[i+1:]
        
        # Recursively get permutations of the remaining string
        for p in uqper(remaining_str):
            # Add the current character to the beginning of each permutation
            perm.append(char + p)
    return perm

s = input("Enter a string: ")
result = uqper(s)
print(result)
