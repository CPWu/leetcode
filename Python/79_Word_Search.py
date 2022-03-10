# 1 Possible Solutions
# 1. DFS + Graph


class Solution:
    # Time: O(M*N*3^L), Space: O(L)
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        
        if not word: 
            return False
        
        rows, cols = len(board), len(board[0])
        visited = set()
        
    
        def dfs(row, col, idx):
            if idx == len(word):
                return True
            
            if row < 0 or row >= rows or col < 0 or col >= cols or word[idx] != board[row][col] or (row, col) in visited:
                return False
            
            visited.add((row, col))
            
            result = (dfs(row + 1, col, idx + 1) or
                    dfs(row - 1, col, idx + 1) or
                    dfs(row, col + 1, idx + 1) or
                    dfs(row, col - 1, idx + 1 ))
            
            visited.remove((row, col))
            return result
            
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False
            