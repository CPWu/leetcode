class Solution(object):
    # Time: O(N), Space: O(1)
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        capacity = s.count(')')
        opened = 0

        for char in s:
            if char == '(':
                if opened == capacity: continue
                opened += 1
            elif char == ")":
                capacity -= 1
                if not opened: continue
                opened -= 1
            
            result.append(char)
        return "".join(result)