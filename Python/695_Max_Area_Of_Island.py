# 1 Possible Solutions
# 1. DFS

class Solution:
    # Time: O(M*N), Space: O(M*N)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Empty Grid
        if not grid:
            return none
        
        area = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = max(area, self.traverseIsland(row, col, grid, visited))
        return area
                    
    
    def traverseIsland(self, row: int, col: int, grid: List[List[int]], visited: set) -> int:
        rows, cols = len(grid), len(grid[0])                
        # Out of Bounds
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0 or (row, col) in visited:
            return 0
        
        visited.add((row, col))
        
        return (1 + 
                self.traverseIsland(row + 1, col, grid, visited) + 
                self.traverseIsland(row - 1, col, grid, visited) + 
                self.traverseIsland(row, col + 1, grid, visited) + 
                self.traverseIsland(row, col - 1, grid, visited)
               )
                      