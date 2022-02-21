# 1 Possible Solutions
# 1. Backtracking

class Solution:
    # Time: O(N*4^n), Space: O(N)
    def letterCombinations(self, digits: str) -> List[str]:
        # Return Result
        result = []

        digitToChar = {
            "0": "",
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def backtrack(i, currentString):
            if len(currentString) == len(digits):
                result.append(currentString)
                return
            
            for character in digitToChar[digits[i]]:
                backtrack(i + 1, currentString + character)
            
        if digits:
            backtrack(0, "")
        
        return result