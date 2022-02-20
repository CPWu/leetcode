class Solution:
    #Time: O(N*2^N), Space: O(N*2^N)
    def letterCasePermutation(self, s: str) -> List[str]:
        result = [[]]
        
        for character in s:
            length = len(result)
            if character.isalpha():
                for i in range(length):
                    result.append(result[i][:])
                    result[i].append(character.lower())
                    result[length + i].append(character.upper())
            else:
                for i in range(length):
                    result[i].append(character)
                    
        return map("".join,result)