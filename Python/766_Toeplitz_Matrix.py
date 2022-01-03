class Solution(object):
    # # Time: O(M*N), Space: O(M+N)
    # def isToeplitzMatrix(self, matrix):
    #     groups = {}
        
    #     for r, row in enumerate(matrix):
    #         for c, val in enumerate(row):
    #             if r-c not in groups:
    #                 groups[r-c] = val
    #             elif groups[r-c] != val:
    #                 return False
    #     return True

    # Time: O(M*N), Space: O(1)  
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True
        