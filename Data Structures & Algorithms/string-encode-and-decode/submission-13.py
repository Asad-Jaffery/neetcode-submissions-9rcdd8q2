class Solution:

    def encode(self, strs: List[str]) -> str:
        # combine each word with its' length followed by a special charecter 
        res = ""
        for word in strs:
            res += str(len(word)) + '#' + word
        return res



    def decode(self, s: str) -> List[str]:
        # look for num (using .isDigit) followed by the special character
        res = []

        while len(s) > 0:
            # get length
            i = 0
            # if len(s) > 1:
            while len(s) > i + 1 and s[i+1] != '#':
                i += 1
            length = int(s[0: i + 1])

            word = s[i + 2: i + 2 + length]
            res.append(word)

            # reduce the size of the string (remove the word we just added)
            s = s[i + 2 + length:]
        return res