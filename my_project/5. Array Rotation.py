# Problem: Rotate array left by k positions
def rotate_left(arr, k):
    if not arr:
        return arr
    
    k = k % len(arr)  # Handle k > array length
    return arr[k:] + arr[:k]

# Test
arr = [1, 2, 3, 4, 5]
k = 2
print(rotate_left(arr, k))  # [3, 4, 5, 1, 2]