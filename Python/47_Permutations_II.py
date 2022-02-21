# 1 Possible Solution
# 1. Backtracking

class Solution:
    # Time: O(N*2^N), Space: O(N)
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Stores the solution
        result = []
        
        # Stores the permutation at computation
        permutation = []
        
        # Equivalent of {n: 0 for n in nums}
        count = Counter(nums)
        
        def dfs():
            if len(permutation) == len(nums):
                result.append(permutation[:])
                return 
            
            for number in count:
                if count[number] > 0:
                    permutation.append(number)
                    count[number] -= 1
                    
                    dfs()
                    
                    count[number] += 1
                    permutation.pop()
                    
        dfs()
        
        return result
                
        