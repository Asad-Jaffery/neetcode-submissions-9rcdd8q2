class Solution:
    def isValid(self, s: str) -> bool:
        # loop through the string, charecter by charcter
        # if the bracket is open, then add it to a stack 


        # if the bracket is closed, pop the stack, and see those two brackets correspond to one another 
            # this requires a dictionary 
            # } : {

        brackets = {"}" : "{", "]" : "[", ")" : "(" }
        stack = []
        for char in s:
            if char in brackets.values():
                stack.append(char)
            else:
                if not stack or stack[-1] != brackets[char]: 
                    return False
                stack.pop()

        if not stack:
            return True
        else:
            return False









        