class Solution(object):
    # Time: O(N), Space: O(1)
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        closeCount = 0
        openCount = 0

        for character in s:
            if closeCount == 0 and character == ')':
                openCount += 1
            else:
                closeCount += 1 if character == "(" else -1
            
        return openCount + closeCount

