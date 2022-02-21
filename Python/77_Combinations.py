# 1 Possible Solutions
# 1. Backtracking

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []

        combination = []

        def backtrack(start, combination):
            if len(combination) == k:
                result.append(combination[:])
                return
            
            # not inclusive therefore n + 1
            for i in range(start, n + 1):
                combination.append(i)
                backtrack(i + 1, combination)
                combination.pop()

        backtrack(1, combination)

        return result