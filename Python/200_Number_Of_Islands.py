# 4 Possible Solutions
# 1. DFS + Visited List
# 2. DFS + Destructive Map
# 3. BFS + Sets

class Solution:
    # DFS + Non-Destructive Map
    # Time: O(M*N), Space: O(M*N)
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check for Empty Grid
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = [[False for col in range(cols)] for row in range(rows)]
        islandCount = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and visited[row][col] == False:
                    # Island may be larger than one cell.
                    self.traverseIsland(row, col, grid, visited)
                    islandCount += 1
        return islandCount
    
    def traverseIsland(self, row: int, col: int, grid: List[List[str]], visited: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        
        # Check to see that grid[row][col] is within bounds and not in the water
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0" or visited[row][col] == True:
            return
        
        # Mark Island as Traversed
        visited[row][col] = True
        
        self.traverseIsland(row + 1, col, grid, visited)
        self.traverseIsland(row - 1, col, grid, visited)
        self.traverseIsland(row, col + 1, grid, visited)
        self.traverseIsland(row, col - 1, grid, visited)

    # DFS + Non-Destructive Map
    # Time: O(M*N), Space: (M*N)
    def numIslands(self, grid: List[List[str]]) -> int:
        # Is the Grid empty
        if not grid:
            return 0
        
        islandCount = 0
        rows, cols = len(grid), len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    self.traverseIsland(row, col, grid)
                    islandCount += 1
        return islandCount
    
    def traverseIsland(self, row: int, col: int, grid: List[List[str]]) -> None:
        rowLimit = len(grid)
        colLimit = len(grid[0])
        
        if row < 0 or row >= rowLimit or col < 0 or col >= colLimit or grid[row][col] == "0":
            return
        
        # Set the grid value to 0 to know we traversed it
        grid[row][col] = "0"
        
        self.traverseIsland(row + 1, col, grid)
        self.traverseIsland(row - 1, col, grid)
        self.traverseIsland(row, col + 1, grid)
        self.traverseIsland(row, col - 1, grid)

    # BFS + Sets
    # Time: O(M*N), Space: (M*N)
    def numIslands(self, grid: List[List[str]]) -> int:
        # Empty Grid
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islandCount = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    self.traverseIsland(row, col, grid, visited)
                    islandCount += 1
        return islandCount
    
    def traverseIsland(self, row, col, grid, visited):
        queue = collections.deque()
        visited.add((row, col))
        queue.append((row, col))
        
        while queue:
            row, col = queue.popleft()
            rows = len(grid)
            cols = len(grid[0])
            directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
            
            for directionR, directionC in directions:
                r, c = row + directionR, col + directionC
                if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited):
                    queue.append((r, c))
                    visited.add((r, c))