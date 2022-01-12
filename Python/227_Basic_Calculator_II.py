class Solution(object):
    # Time: O(N), Space: (N)
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
    
        # Check for empty string:
        if not s:
            return 0
        
        stack, current_number, operator = [], 0, "+"
        # All Possible Operators
        all_operators = {"+","-","*","/"}
        # All Possible Digits
        nums = set(str(x) for x in range(10))
        
        for index, character in enumerate(s):
            if character in nums:
                current_number = current_number * 10 + int(character)
            if character in all_operators or index == len(s) - 1:
                if operator == "+":
                    stack.append(current_number)
                elif operator == "-":
                    stack.append(-current_number)
                elif operator == "*":
                    stack[-1] *= current_number
                elif operator == "/":
                    if stack[-1] >=0 :
                         stack[-1] //= current_number
                    else:
                         stack[-1] = -(-stack[-1]//current_number)
                
                current_number = 0
                operator = character
        return sum(stack)