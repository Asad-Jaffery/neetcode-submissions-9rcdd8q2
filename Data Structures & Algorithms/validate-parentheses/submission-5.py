class Solution:
    def isValid(self, s: str) -> bool:
        # if its an opening parenthesis, we add it to a stack

        # if its a closing parenthesis, we pop the stack

          # if the pop is not the corresponding opening parenthesis, its false

        mapping = {')': '(', '}': '{', ']':'['}


        stack = []
        while len(s) > 0:
            curr = s[0]
            s = s[1:]
            if curr in mapping:
                if (not stack) or (mapping[curr] != stack.pop()):
                    return False
            else: 
                stack.append(curr)
            
        return not stack # this is key
        







        