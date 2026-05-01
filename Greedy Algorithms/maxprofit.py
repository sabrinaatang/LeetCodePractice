'''
Phase 1: You are tracking the price of a single stock. You are given an array prices where prices[i] is the price on the ith day. You want to maximize your profit by choosing one single day to buy and a different day in the future to sell. Return the max profit. If no profit is possible, return 0.
Standard: [7, 1, 5, 3, 6, 4] → Output: 5
Downward Trend: [7, 6, 4, 3, 1] → Output: 0
Late Peak: [2, 4, 1] → Output: 2
'''

def maxProfit(prices: list[int]) -> int:
    """
    Goal: Find the maximum profit possible with UNLIMITED transactions.
    """
    # Write your code here
	
    mn = prices[0]
    runningDiff = 0
	
    for r in range(1, len(prices)):
        if prices[r] < mn:
            mn = prices[r]
        runningDiff = max(runningDiff, prices[r] - mn)
    return runningDiff
	# Standard: [7, 1, 5, 3, 6, 4] → Output: 5
	# Late Peak: [2, 4, 1] → Output: 2
	#Downward Trend: [7, 6, 4, 3, 1] → Output: 0

		
'''
Phase 2
The rules have changed. You can now complete as many transactions as you want. You can buy and sell multiple times to stack profits. The only constraint: You must sell your current stock before you can buy again.
📥 Test Data
Standard: [7, 1, 5, 3, 6, 4] → Output: 7 (4 + 3)
Trend: [1, 2, 3, 4, 5] → Output: 4 # 
Volatile: [1, 5, 1, 5] → Output: 8 ( 4 + 4 )
'''
def maxProfit(prices: list[int]) -> int:
    """
    Goal: Find the maximum profit possible with UNLIMITED transactions.
    """
    # Write your code here
    runningTotal = 0
    mn = prices[0]
    for r in range(1, len(prices)):
        if prices[r] > prices[r - 1]:
            runningTotal += prices[r] - prices[r-1]
    return runningTotal

# Test Cases
# arr = [7, 1, 5, 3, 6, 4]
# print(maxProfit(arr)) 


'''
 Phase III: The Cooldown
LeetCode 309: Best Time to Buy and Sell Stock with Cooldown
📝 Mentee Introduction
"Unlimited transactions are still allowed, but after you sell a stock, you cannot buy on the very next day. You must wait at least one full day (cooldown) before buying again."

Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0
'''

def maxProfit(prices: list[int]) -> int:
    """
    Goal: Maximize profit with unlimited transactions and a 1-day cooldown.
    """
    maxProfit = 0
    mn = prices[0]
    r = 1
    while r < len(prices):
        if prices[r-1] < prices[r]:
            maxProfit += prices[r] - prices[r-1]
            r += 1
        r += 1
        
    return maxProfit


prices = [1,2,3,0,2]
print("Test Case 1: ", maxProfit(prices))
correct = 3
print("True" if maxProfit(prices) == correct else "False")

prices = [1]
print("Test Case 2: ", maxProfit(prices))
correct = 0
print("True" if maxProfit(prices) == correct else "False")