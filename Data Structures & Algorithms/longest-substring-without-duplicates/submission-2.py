class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # l and r pointer 
        # use a set to keep track of the chars

        # while r is less than the length of the string: 
            # if r + 1 is not in the set,
              # r += 1 
              # increase the res 
              # add the new r in the set 
            # else: 
                # increment l until either l == r or until the size of the subarrya is 1 


        if not s: 
            return 0

        curr = set()
        res = 0
        l, r = 0, 0

        while r < len(s):
            if s[r] not in curr: 
                curr.add(s[r])
                res = max(res, len(curr))
                r += 1
            else: 
                while s[r] in curr and l < r: 
                    curr.remove(s[l])
                    l += 1
                
        return res


