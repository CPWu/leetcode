class Solution(object):
    # Time: O(N), Space: O(1)
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        wordPointer = 0
        abbrPointer = 0

        while wordPointer < len(word) and abbrPointer < len(abbr):
            if abbr[abbrPointer].isalpha():
                if abbr[abbrPointer] != word[wordPointer]:
                    return False
                abbrPointer += 1
                wordPointer += 1
            else:
                if abbr[abbrPointer] == '0':
                    return False
                tempValue = 0
                while abbrPointer < len(abbr) and abbr[abbrPointer].isdigit():
                    tempValue = tempValue * 10 + int(abbr[abbrPointer])
                    abbrPointer += 1
                wordPointer += tempValue

        return abbrPointer == len(abbr) and wordPointer == len(word)
        
        
soln = Solution()
word = "internationalization"
abbr = "i12iz4n"
print(soln.validWordAbbreviation(word, abbr))
