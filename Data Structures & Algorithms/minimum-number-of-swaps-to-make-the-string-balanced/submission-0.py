class Solution:
    def minSwaps(self, s: str) -> int:
        issues = 0
        max_issues = 0
        for i in range(len(s)):
            if s[i] == "]":
                issues += 1
            else:
                issues -= 1
            max_issues = max(max_issues, issues)


        if max_issues % 2 == 0: 
            return int(max_issues / 2)
        else:
            return int((max_issues + 1) / 2)
        # how many closing before opening do we have 






        