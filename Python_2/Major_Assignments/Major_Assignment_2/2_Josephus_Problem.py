# Recursive function to solve the Josephus problem
def josephus(n, k):
    if n == 1:  # Base case
        return 0
    return (josephus(n - 1, k) + k) % n  # Recursive formula

'''Recursive Function: Time complexity is O(n)'''

# Iterative function to solve the Josephus problem
def josephus_iterative(n, k):
    result = 0
    for i in range(2, n + 1):
        result = (result + k) % i
    return result

n=6
k=8
print(josephus(n,k))
print(josephus_iterative(n,k))

'''Iterative Function: Time complexity is also O(n)'''


'''Comparison
The iterative version is more efficient as it avoids the overhead of recursive calls and uses constant space (O(1)), while the recursive version uses additional stack space (O(n)).
'''