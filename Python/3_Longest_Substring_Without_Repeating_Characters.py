class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # If string is empty
        if not s:
            return 0
        
        # Dictionary to store characters
        characterDict = {}
        characterSet = set()
        result = 0
        leftPointer = 0
        
        for iterator in range(len(s)):
            while s[iterator] in characterSet:
                characterSet.remove(s[leftPointer])
                leftPointer += 1
            characterSet.add(s[iterator])
            result = max(result, iterator - leftPointer + 1)
        return result