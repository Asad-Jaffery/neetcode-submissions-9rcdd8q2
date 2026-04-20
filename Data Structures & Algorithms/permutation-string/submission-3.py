class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create a sliding window of size of s1
        # sort the string every time, if == to s1(sorted), then return true

        # at the end, return false


        l = 0
        r = len(s1) - 1

        s1_sorted = sorted(s1)

        while r < len(s2):
            temp = s2[l: r + 1]
            if sorted(temp) == s1_sorted:
                return True
            else: 
                l += 1
                r += 1
        return False






        