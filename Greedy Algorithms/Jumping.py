def can_jump(nums: list[int]) -> bool:
    # Your code here
	max_jump = 0
	n = len(nums)
	for ind, num in enumerate(nums):
		print( ind, " ", max_jump)
		if ind > max_jump:
			print("here")
			return False
		max_jump = max(max_jump, num + ind)
		if max_jump > n:
			print("returning True")
			return True
	return True
			

# Test Cases
# print(can_jump([2, 3, 1, 1, 4])) # Expected: True
# print(can_jump([3, 2, 1, 0, 4])) # Expected: False

def jump(nums: list[int]) -> int:
    # Logic: Count the "windows" or "waves" of reach
    max_jump = 0
    jumps = 0
    n = len(nums)
    current_jump_end = 0
    for ind, num in enumerate(nums):
        if ind == n - 1:
            break
        max_jump = max(max_jump, num + ind)
        # print("Max: ", max_jump)
        if ind == current_jump_end:
            jumps += 1
            current_jump_end = max_jump
            # print(ind, " ", current_jump_end)

    return jumps


# Test Case:
# nums = [2, 3, 1, 1, 4] -> Output: 2
# nums = [2, 3, 1, 1, 4]
# print(jump(nums))

# Test Case:
# nums = [5, 2, 1, 0, 4] -> Output: 1
# nums = [5, 2, 1, 0, 4]
# print(jump(nums))


def max_sub_array(nums: list[int]) -> int:
    # Logic: If your current sum becomes worse than just starting 
    # fresh with the current number, reset!
    res = float('-inf')
    maxEnding = float('-inf')
    n = len(nums)
    for i in range(n):
          maxEnding = max(maxEnding + nums[i], nums[i])
          res = max(maxEnding, res)
    return res
          

# Test Case:
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> Output: 6
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sub_array(nums))

# Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
# Output: 11
# Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.
arr = [2, 3, -8, 7, -1, 2, 3]
print(max_sub_array(arr))

# Input: arr[] = [-2, -4]
# Output: -2
# Explanation: The subarray [-2] has the largest sum -2.
arr = [-2, -4]
print(max_sub_array(arr))

# Input: arr[] = [5, 4, 1, 7, 8]
# Output: 25
# Explanation: The subarray [5, 4, 1, 7, 8] has the largest sum 25.
arr = [5, 4, 1, 7, 8]
print(max_sub_array(arr))
