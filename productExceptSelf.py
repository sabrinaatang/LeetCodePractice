from typing import List
def productExceptSelf(nums: List[int]) -> List[int]:
    prod, zero_cnt = 1, 0
    for num in nums:
        if num:
            prod *= num
        else:
            zero_cnt += 1

    if zero_cnt > 1:
        return [0] * len(nums)
    
    res = [0] * len(nums)
    for i, c in enumerate(nums):
        if zero_cnt:
            res[i] = 0 if c else prod
        else:
            res[i] = prod // c
    return res

# Test Case #1
# Output: [48,24,12,8]
nums = [1,2,4,6]
print(productExceptSelf(nums))

# Test Case #2
# Output: [0,-6,0,0,0]
nums = [-1,0,1,2,3]
print(productExceptSelf(nums))

# Test Case #3
# Output: [0, 0, 0, 0, 0, 0]
nums = [0,1,0,4,4,5]
print(productExceptSelf(nums))
