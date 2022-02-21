class Solution:
    # Time: O(2^t), Space: O(2^t)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(i, currentList, total):
            if total == target:
                result.append(currentList[:])
                return
            
            if i >= len(candidates) or total > target:
                return
            
            candidates[i]
            
            currentList.append(candidates[i])
            
            backtrack(i, currentList, total + candidates[i])
            currentList.pop()
            backtrack(i + 1, currentList, total)
        
        backtrack(0, [], 0)
        
        return result