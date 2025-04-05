# Linear search to extract suspicious transactions
def extract_suspicious(transactions, threshold):
    return [t for t in transactions if t > threshold]

# Selection sort to sort suspicious transactions
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Binary search to find a specific transaction
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Merge sort to sort all transactions
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

transactions = [120, 45, 300, 220, 90, 600, 130, 75, 800, 500, 350, 40]
threshold = 250
suspicious = extract_suspicious(transactions, threshold)
print("Suspicious Transactions:", suspicious)

sorted_suspicious = selection_sort(suspicious)
print("Sorted Suspicious Transactions:", sorted_suspicious)

search_amount = 500
found = binary_search(sorted_suspicious, search_amount)
print(f"Is {search_amount} in the suspicious list? {found}")

sorted_transactions = merge_sort(transactions)
print("Sorted Transactions:", sorted_transactions)