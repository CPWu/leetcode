# 3 Possible Solutions
# 1. Using a Stack
# 2. Two Pass String Builder
# 3. Shortened Two Pass String Builder

class Solution:
    # Time: O(N), Space: O(N)
    def minRemoveToMakeValid(self, s: str) -> str:
        indexesToRemove = set()
        stack = []
        
        for index, character in enumerate(s):
            # Character is alpha, so skip
            if character not in "()":
                continue
            
            # If character is opening parentheses
            if character == "(":
                stack.append(index)
            # If character is closing parentheses and stack empty.
            elif not stack:
                indexesToRemove.add(index)
            # If character is closing parentheses
            else:
                stack.pop()
            
        indexesToRemove = indexesToRemove.union(set(stack))
        stringBuilder = []

        for idx, char in enumerate(s):
            if idx not in indexesToRemove:
                stringBuilder.append(char)
        return "".join(stringBuilder)

    # Time: O(N), Space: O(N)
    def minRemoveToMakeValid(self, s: str) -> str:
        firstPassChars = []
        balance = 0
        openParentheses = 0

        for character in s:
            if character == "(":
                balance += 1
                openParentheses += 1
            if character == ")":
                if balance == 0:
                    continue
                balance -= 1
            firstPassChars.append(character)
     
        result = []
        openToKeep = openParentheses - balance
        
        for character in firstPassChars:
            if character == "(":
                openToKeep -= 1
                if openToKeep < 0:
                    continue
            result.append(character)
            
        
        return "".join(result)

    # Time: O(N), Space: O(N)
    def minRemoveToMakeValid(self, s: str) -> str:
        firstPass = []
        balance = 0
        openSeen = 0
        
        for character in s:
            if character == "(":
                balance += 1
                openSeen += 1
            if character == ")":
                if balance == 0:
                    continue
                balance -= 1
            firstPass.append(character)
        
        result = []
        openToKeep = openSeen - balance
        for character in firstPass:
            if character == "(":
                openToKeep -= 1
                if openToKeep < 0:
                    continue
            result.append(character)
            
        
        return "".join(result)