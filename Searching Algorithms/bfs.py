'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],
                [1,1,0],
                [0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],
                [0,1,1],
                [1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

'''
from collections import deque
def rotten_oranges(array):
    res = 0
    rows = len(array)
    cols = len(array[0])
    q = deque()
    for i in range(rows):
        for j in range(cols):
            if array[i][j] == 2:
                dxdy = [ (0, 1), (1, 0), (-1, 0), (0, -1)]
                for dx, dy in dxdy:
                    newRow = i + dx
                    newCol = j + dy
                    print("new: ", newRow, newCol)
                    if newRow < 0 or newRow >= rows or newCol < 0 or newCol >= cols or array[newRow][newCol] == 0:
                        continue
                    if array[newRow][newCol] == 1:
                        print("found fresh")
                        q.append((newRow, newCol))
                if q:
                    print("Queue not empty")
                    res += 1
                while q:
                    row, col = q.pop()
                    array[row][col] = 2
            
    for i in range(rows):
        for j in range(cols):
            if array[i][j] == 1:
                return -1
    return res

# grid = [[2,0,1,1,1,1,1,1,1,1],
#         [1,0,1,0,0,0,0,0,0,1],
#         [1,0,1,0,1,1,1,1,0,1],
#         [1,0,1,0,1,0,0,1,0,1],
#         [1,0,1,0,1,0,0,1,0,1],
#         [1,0,1,0,1,1,0,1,0,1],
#         [1,0,1,0,0,0,0,1,0,1],
#         [1,0,1,1,1,1,1,1,0,1],
#         [1,0,0,0,0,0,0,0,0,1], 
#         [1,1,1,1,1,1,1,1,1,1]]
# Test Case
# grid = [[2,1,1],
#                 [1,1,0],
#                 [0,1,1]]
# Output: 4
# print(rotten_oranges(grid))
#Test Case 
# grid = [[0,2]]
# print(rotten_oranges(grid))
# Output: -1

# Test Case
# grid = [[2,1,1],
#         [0,1,1],
#         [1,0,1]]
# Output: -1
# print(rotten_oranges(grid))

'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = "2"
Output: ["a","b","c"]

'''
def letter_combination(digits: str) -> list[str]:
    mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result = []
    combos = deque()
    combos.append("")
    while combos:
        prefix = combos.popleft()
        print("Prefix: ", prefix, len(prefix))
        if len(prefix) == len(digits):
            result.append(prefix)
            continue

        prefix_length = len(prefix)
        digit = digits[prefix_length]

        if int(digit) < 2 or int(digit) > 9:
            continue
        for char in mapping[digit]: # "wxyz"
            combos.append(prefix + char)

    return result

#Test Case 1
# digits = "23"
#Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# print(letter_combination(digits))

#Test Case 2
# digits = "2"
# Output: ["a","b","c"]
# print(letter_combination(digits))
