def twoSum(nums, k):
    mp = {}
    for i in range(len(nums)):
        if k - nums[i] in mp:
            return (mp[k-nums[i]], i)
        mp[nums[i]] = i
    return -1