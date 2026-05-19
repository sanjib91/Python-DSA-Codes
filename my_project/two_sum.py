nums = [1,2,7,11,15]

def two_sum_II(nums, target):
    left, right = 0, len(nums) -1 
    while left < right:
        if nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left += 1

        elif nums[left] + nums[right] == target:
            return [nums[left], nums[right]]

print(two_sum_II(nums, 18))                

