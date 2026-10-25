class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep app letters in a hash set, as we traverse 

        # traverse using a l and r pointer? 
        # r increases until we see a diplicate
            # if we see a duplicate, we keep incresing l (and removing thos chars from the set) until no more 
                # duplicates OR l = r

        l, r = 0, 0
        curr_chars = set()

        max_substring = 0 

        while r < len(s):
            curr = s[r]
            if s[r] in curr_chars:
                curr_chars.remove(s[l])
                l += 1

            else: 
                curr_chars.add(s[r])
                r += 1

            
            max_substring = max(max_substring, len(curr_chars))
        

        return max_substring





        