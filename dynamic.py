'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0


pseudo
change = 0
mn = float("inf") 
def recur(amount, change): #coins = [1,2,5], amount = 11

    if amount == 0:
        mn = min(mn, change)r
        return mn

    if amount < 0:
        return mn
    for coin in coins:
        return recur(amount - coin, change + 1) # recur(11-1, 1), recur(11-2, 1), recur(11-5, 1), recur(10-1, 2)...recur(0, 11), recur(-1, 6), recur(6, 1), recur(1, 2)

change = recur(11, 0)
return change
'''
class Solution: 
    def coinChange(self, coins, amount) -> int:
        mn = float("inf") 
        dp = {}
        def recur(amount, change): #coins = [1,2,5], amount = 11
            nonlocal mn
            if amount in dp:
               return dp[amount]

            if amount == 0:
                mn = min(mn, change)
                return 0

            if amount < 0:
                return mn
            for coin in coins:
                #print('here', coin)
                if amount - coin >= 0:
                    mn = min(mn, recur(amount - coin, change + 1)) # recur(11-1, 1), recur(11-2, 1), recur(11-5, 1), recur(10-1, 2)...recur(0, 11), recur(-1, 6), recur(6, 1), recur(1, 2)
            dp[amount] = mn
            return dp[amount]

        change = recur(11, 0)
        if change != float("inf"):
            return change
        return -1
        
solution = Solution()    
coins = [1,2,5]
amount = 11      
print(solution.coinChange(coins, amount)) # Output: 3

'''
     1.              2.               5 
   /.
  1  2  5.        1.  2.  5.        1.  2   5

'''

class Solution:
    def coinChange(self, coins, amount) -> int:
        dp = {}

        def recur(amount):
            # Base cases
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")  # Invalid path
            
            # Return cached result
            if amount in dp:
                return dp[amount]

            # Try every coin, take the minimum result
            best = float("inf")
            for coin in coins:
                result = recur(amount - coin)
                if result != float("inf"):
                    best = min(best, result + 1)  # +1 for the coin we just used

            dp[amount] = best
            return dp[amount]

        answer = recur(amount)
        return answer if answer != float("inf") else -1
    

  