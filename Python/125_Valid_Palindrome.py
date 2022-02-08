# 4 Possible Solutions
# 1. Compare with Reverse - String
# 2. Compare with Reverse - List
# 3. Recursion
# 4. Two Pointers


class Solution(object): 
    # Time: O(N^2), Space: O(N)
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        reversedString = ""
        s = s.lower()
        
        for character in s:
            if character.isalnum():
                # String Concat = N * N
                # Concat requires iterating over string 'reversedString' every loop before appending,thus the complexity.
                reversedString += character.lower()
        return reversedString == reversedString[::-1]

    # Time: O(N), Space: O(N)
    def isPalindrome(self, s):
        reversedChars = []
        for i in range(len(s)):
            reversedChars.append(s[i])
        return s == "".join(reversedChars)
    
    # Time: O(N), Space: O(N) 
    def isPalindrome(self, s, i = 0):
        j = len(s) - 1 - i
        return True if i >= j else s[i] == s[j] and self.isPalindrome(s, i + 1)

    # Time: O(N), Space: O(1)
    def isPalindrome(self, s):
        leftIdx = 0
        rightIdx = len(s) - 1
        s = s.lower()

        while leftIdx < rightIdx:
            if s[leftIdx].isalnum() == False:
                leftIdx += 1
            elif s[rightIdx].isalnum() == False:
                rightIdx -= 1
            elif s[leftIdx] != s[rightIdx]:
                return False
            else:
                leftIdx += 1
                rightIdx -= 1
        return True 

    def printListString(self, s):
        indexValue = 3
        #print(s[indexValue])

soln = Solution()
s = "A man, a plan, a canal: Panama"
print(soln.isPalindrome(s))

print(soln.printListString(s))