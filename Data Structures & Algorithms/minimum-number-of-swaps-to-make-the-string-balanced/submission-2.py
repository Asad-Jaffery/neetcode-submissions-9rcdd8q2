class Solution:
    def minSwaps(self, s: str) -> int:
        bad_brackets, max_bad_brackets = 0, 0

        for i in range(len(s)):
            if s[i] == "[":
                bad_brackets -= 1
            else: 
                bad_brackets += 1
            max_bad_brackets = max(max_bad_brackets, bad_brackets)
        
        if max_bad_brackets % 2 == 0: 
            return int(max_bad_brackets / 2)
        else: 
            return int((max_bad_brackets + 1) / 2)

        