nums = [1,1,1,2,2,3,3,3,4,5,5,5,6,6,7,7,7,7,7]

def remove_duplicates(nums):
    stack = []
    for num in nums:
        if num not in stack:
            stack.append(num)

    return stack

print(remove_duplicates(nums))