class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        "zxyzxyz"
        "zxy"
        
        # while z is in chars, increse l

        
        # chars

        chars = set()
        longest = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                longest = max(longest, len(chars))
                r += 1
            else: 
                while s[r] in chars:
                    chars.remove(s[l])
                    l += 1
        
        return longest



        