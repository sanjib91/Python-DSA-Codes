nums = [1,2,7,11,15]

def two_sum_II(arr, target):
    left, right = 0 , len(arr) - 1
    while left < right:
        if arr[left] + arr[right] > target:
            right -= 1
        elif arr[left] + arr[right] < target:
            left += 1
        elif arr[left] + arr[right] == target:
            return [arr[left], arr[right]]

print(two_sum_II(nums, 18)) 