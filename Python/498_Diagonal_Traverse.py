class Solution:
    
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # Check for empty matrices
        if not matrix or not matrix[0]:
            return []
        
        # Variables to track the size of the matrix
        # rows
        rows = len(matrix) #m
        cols = len(matrix[0]) #n
        
        # Indices to progress through matrix
        row_index = 0
        col_index = 0
        
        # Direction variable
        # 1 is up
        # 0 is down
        direction = 1
        
        # result 
        answer = []
            
        while row_index < rows and col_index < cols:
            answer.append(matrix[row_index][col_index])
            
            # Move along in the current diagonal depending upon
            # the current direction.[x, y] -> [x - 1, y + 1] if 
            # going up and [x, y] -> [x + 1][y - 1] if going down.
            new_row_index = row_index + (-1 if direction == 1 else 1)
            new_column_index = col_index + (1 if direction == 1 else -1)
            
            if new_row_index < 0 or new_row_index == rows or new_column_index < 0 or new_column_index == cols:
                # If the current diagonal was going in the upwards
                # direction.
                if direction:
                    # For an upwards going diagonal having [x, y] as its tail
                    # If [x, y + 1] is within bounds, then it becomes
                    # the next head. Otherwise, the element directly below
                    # i.e. the element [i + 1, j] becomes the next head
                    row_index = row_index + (col_index == cols - 1)
                    col_index = col_index + (col_index < cols - 1)
                else:
                    # For a downwards going diagonal having [x, y] as its tail
                    # if [x + 1, y] is within bounds, then it becomes
                    # the next head. Otherwise, the element directly below
                    # i.e. the element [x, y + 1] becomes the next head
                    col_index += (row_index == rows - 1)   
                    row_index += (row_index < rows - 1)   
  
                # Flip the direction
                direction = 1 - direction        
            else:
                row_index = new_row_index
                col_index = new_column_index
                        
        return answer                 