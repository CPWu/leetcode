class Solution:
    # Time: O(N), Space: O(N)
    def isValid(self, s: str) -> bool:
        
        # Empty stack needed to keep track of open brackets
        stack = []
        
        # Dictionary required to keep track of a closing bracket against a matching open brakcet
        bracketDictionary = {")": "(", "}": "{", "]": "["}
        
        # For every bracket in the expression
        for character in s:
            # Pop the topmost element from the stack, if it is non empty
            # Otherwise assign a dummy value of '#' to the top_element variable
            if character in bracketDictionary:
                top_element = stack.pop() if stack else '#'
                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if bracketDictionary[character] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(character)
        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack