# 1 Possible Solution
# 1. Backtracking

class Solution:
    # Time: O(N*2^N), Space: O(N*N!)
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.permutationsHelper(0, nums, permutations)
        return permutations
    
    def permutationsHelper(self, i, nums, permutations):
        if i == len(nums):
            permutations.append(nums[:])
        else:
            for j in range(i, len(nums)):
                self.swap(nums, i, j)
                self.permutationsHelper(i + 1, nums, permutations)
                self.swap(nums, i, j)
    
    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]