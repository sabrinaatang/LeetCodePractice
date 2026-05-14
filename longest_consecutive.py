from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        mx = 0
        
        for num in nums:
            length = 1
            if (num - 1) not in nums:
                length = 1
                while num + length in nums:
                    length += 1
                mx = max(mx, length)
        return mx
    
solution = Solution()

# Test Case #1
nums = [0,3,2,5,4,6,1,1]
#Output: 7
print(solution.longestConsecutive(nums))


# Test Case #2
nums = [2,20,4,10,3,4,5]
#Output: 4
print(solution.longestConsecutive(nums))

# Test Case #3
nums = []
#Output: 0
print(solution.longestConsecutive(nums))

# Test Case #4
nums = [0]
#Output: 1
print(solution.longestConsecutive(nums))

# Time Complexity: O(n) --> Creating a set requires O(n) time for creation and O(1) time for constant item lookup
# Space Complexity: O(n) --> creating a set from nums uses O(n) space