# Recursive function to compute the sum of the first n natural numbers
def recursive_sum(n):
    if n == 0:  # Base case
        return 0
    return n + recursive_sum(n - 1)  # Recursive step
'''Recursive Function: Time complexity is O(n)'''

# Iterative function to compute the sum of the first n natural numbers
def iterative_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n=12
print(recursive_sum(n))
print(iterative_sum(n))


'''Iterative Function: Time complexity is also O(n)'''


''' Comparison
Recursion is less efficient because it involves function call overhead and uses additional stack space (space complexity is O(n)).
Iteration is more efficient as it avoids the overhead of recursive calls and uses constant space (O(1)).
'''