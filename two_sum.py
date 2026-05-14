def twoSum(nums, k):
    mp = {}
    for i in range(len(nums)):
        if k - nums[i] in mp:
            return (mp[k-nums[i]], i)
        mp[nums[i]] = i
    return -1

# Two Integer Sum II
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        n = len(numbers)
        while l < r:
            # check if current pair returns target
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            # if l
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return [l, r]