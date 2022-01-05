class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        # Time: O(N), Space: O(N)
        for character in s:
            if stack and stack[-1]==character:
                stack.pop()
            else:
                stack.append(character)
        
        return "".join(stack)
        
        
soln = Solution()
s = "abbaca"
print(soln.removeDuplicates(s))
