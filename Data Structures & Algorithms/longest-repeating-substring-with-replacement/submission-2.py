class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
         # we increase r if the window is valid
        # we increase l if the window is not valid

        # valid means the window_size - max_char_counts >= k

        # how do i get the max character? 


        d = {char: 0 for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
        l, r = 0, 0
        res = 0
        

        while r <= len(s) - 1:
            d[s[r]] += 1 
            most_freq = max(d, key=d.get)
            if (r - l + 1) - d[most_freq] <= k:
                res = max(res, r - l + 1)
                r += 1
            else:
                d[s[l]] -= 1
                l += 1
                r += 1
        return res
        


