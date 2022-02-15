# 1 Possible Solutions
# 1. Backtracking

class Solution:
    # Time: O(N*2^N), Space: O(N)
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        partitions = []
        
        def dfs(i):
            if i >= len(s):
                result.append(partitions.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    partitions.append(s[i:j+1])
                    dfs(j+1)
                    partitions.pop()
                    
        dfs(0)
        return result
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r, = l+1, r-1
        return True