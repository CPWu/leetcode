class Solution:
    # Time: O(2^t), Space: O(N)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []

        def backtrack(position , currentCombo, target):
            if target == 0:
                result.append(currentCombo[:])
                return
            
            if target <= 0:
                return

            prev = -1
            for i in range(position, len(candidates)):
                if candidates[i] == prev:
                    continue
        
                currentCombo.append(candidates[i])
                backtrack(i + 1, currentCombo, target - candidates[i])
                currentCombo.pop() 
                prev = candidates[i]
        
        backtrack(0, [], target)

        return result
