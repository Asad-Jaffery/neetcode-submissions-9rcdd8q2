class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currLetters = set()
        maxLength = 0
        l, r = 0, 0

        while r < len(s):
            if s[r] in currLetters:
                currLetters.remove(s[l])
                l += 1
            else:
                currLetters.add(s[r])
                r += 1
            maxLength = max(maxLength, len(currLetters))

        return maxLength





        