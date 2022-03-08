# 1 Possible Solutions
# 1. Two Pointer

class Solution(object):
    # Time: O(N), Space(1)
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """    
        leftPointer = 0
        rightPointer = len(s) - 1

        while leftPointer < rightPointer:
            if s[leftPointer] != s[rightPointer]:
                return self.isPalindrome(s, leftPointer+1, rightPointer) or self.isPalindrome(s, leftPointer, rightPointer - 1)
            leftPointer += 1
            rightPointer -= 1

        return True

    def isPalindrome(self, s, leftPointer, rightPointer):
        while leftPointer < rightPointer:
            if s[leftPointer] != s[rightPointer]:
                return False
            leftPointer += 1
            rightPointer -= 1
        return True

soln = Solution()
s = "abc"
print(soln.validPalindrome(s))
