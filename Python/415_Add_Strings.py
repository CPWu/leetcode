class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Time: O(max(N1, N2)), Space: O(max(N1, N2)+1)
        i = len(num1) - 1
        j = len(num2) - 1

        carry = 0
        result = ""

        while i >=0 or j >= 0 or carry > 0:
            if i >= 0:
                carry += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                carry += ord(num2[j]) - ord('0')
                j -= 1
            result += str(carry%10)
            carry = carry // 10

        return result[::-1]
            
        
soln = Solution()
s1 = "2859"
s2 = "293"
print(soln.addStrings(s1, s2))
