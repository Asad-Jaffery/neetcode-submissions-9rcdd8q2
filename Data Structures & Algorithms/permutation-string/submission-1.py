class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = list(s1)
        s1_chars = sorted(s1_chars)
     
        s1_len = len(s1)
        l, r = 0, s1_len - 1

        while r < len(s2):
            currChars = []
            for i in range(s1_len):
                if s2[l + i] in s1_chars:
                    currChars.append(s2[l + i])
            if sorted(currChars) == s1_chars:
                return True
            else:
                r += 1
                l += 1

        return False







        