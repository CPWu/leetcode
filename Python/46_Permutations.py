# 1 Possible Solution
# 1. Backtracking

class Solution:
    # Time: O(N*2^N), Space: O(N*N!)
    def permutations(nums):
        if not nums:
            return []
        
        def backtrack(Idx = 0):
            if Idx == lengthOfNums:
                result.append(nums[:])
            for j in range(Idx, lengthOfNums):
                swap(nums, Idx, j)
                backtrack(Idx + 1)
                # backtrack
                swap(nums, Idx, j)
                
        def swap(array, x, y):
            array[x], array[y] = array[y], array[x]
            
        result = []
        lengthOfNums = len(nums)
        backtrack()
        return result

    # Python Slicing
    def getPermutations(array):
        permutations = []
        permutationsHelper(array, [], permutations)
        return permutations

    def permutationsHelper(array, currentPermutation, permutations):
        if not len(array) and len(currentPermutation):
            permutations.append(currentPermutation)
        else:
            for i in range(len(array)):
                newArray = array[:i] + array[i + 1 :]
                newPermutation = currentPermutation + [array[i]]
                permutationsHelper(newArray, newPermutation, permutations)