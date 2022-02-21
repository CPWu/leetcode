# 1 Possible Solutions
# 1. Backtracking

class Solution:
    # Time: O(N*2^N), Space: O(n log n)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Solution result
        result = []

        # Sort Array
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                result.append(subset[:])
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # All subsets that dont include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            backtrack(i + 1, subset)

        backtrack(0, [])

        return result



        



    