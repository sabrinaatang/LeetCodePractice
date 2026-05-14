class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join(char.lower() for char in s if char.isalnum())
        return res == res[::-1]
    
sol = Solution()
# Test Case 
# Output: True
s = "Was it a car or a cat I saw?"
print(sol.isPalindrome(s))

# Test Case 
# Output: False
s = "tab a cat"
print(sol.isPalindrome(s))