# 2 Possible Solutions
# 1. Cheat using .reverse()
# 2. Backtracking

class Solution:
    # Time: O(N * 2^N), Space: O(N)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        subset = []

        def backtrack(i):
            # Out of bounds
            if i >= len(nums):
                result.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # decision not to include nums[i]
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return result