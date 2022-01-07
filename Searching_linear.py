def linear_search (A, key):
    index = 0
    while index < len(A):
        if A[index] == key:
            return index
        index = index + 1
    return -1

A = [14, 67, 34, 65, 87]
found = linear_search(A, 34)
print('Result:', found)
