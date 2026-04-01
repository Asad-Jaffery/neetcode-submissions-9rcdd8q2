class Solution:
    def isValid(self, s: str) -> bool:
        # open bracket -> add to stack
        # close bracket -> pop top of stack
            # if close bracket does not correspond top of stack -> return false

        # return true


        matches = {")" :  "(", "]" : "[", "}" : "{"}
        stack = []
        for i in range(len(s)):
            if s[i] in matches.values():
                stack.append(s[i])
            elif s[i] in matches: 
                if not stack:
                    return False
                top = stack.pop() # should be opening bracket 
                if matches[s[i]] != top:
                    return False
        if not stack:
            return True
        else: 
            return False










        