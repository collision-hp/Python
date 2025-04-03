# Recursive function for exponentiation by squaring
def fast_power(a, b):
    if b == 0:  # Base case
        return 1
    if b % 2 == 0:  # If b is even
        half = fast_power(a, b // 2)
        return half * half
    else:  # If b is odd
        return a * fast_power(a, b - 1)

# Iterative function for exponentiation by squaring
def fast_power_iterative(a, b):
    result = 1
    while b > 0:
        if b % 2 == 1:  # If b is odd
            result *= a
        a *= a  # Square the base
        b //= 2  # Halve the exponent
    return result

a=9
b=8
print(fast_power(a,b))
print(fast_power_iterative(a,b))

'''Time Complexity
Naive Recursive Method: Time complexity is O(b) because it makes b recursive calls.
Exponentiation by Squaring: Time complexity is O(log b) because the exponent is halved in each step.
'''

'''Comaprison
The optimized recursive method and the iterative method both have the same time complexity (O(log b)), but the iterative method is more efficient in terms of space (O(1) vs. O(log b) for recursion).
'''