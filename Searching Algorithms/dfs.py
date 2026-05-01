def letter_combination( digits: str) -> list[str]:
    if not digits:
        return []

    mapping = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
    result = []

    def dfs(index, prefix):
        if index == len(digits):
            result.append(prefix)
            return

        for char in mapping[digits[index]]:
            dfs(index + 1, prefix + char)

    dfs(0, "")
    return result



#Test Case 1
digits = "23"
#Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(letter_combination(digits))

#Test Case 2
digits = "2"
# Output: ["a","b","c"]
print(letter_combination(digits))