arr = [4,1,2,4,5,1,3,5,4,7,9,8]

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []    

print(two_sum(arr,6))    