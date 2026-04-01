class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # get all characters and put them into a set
            # make the set a key of a map 

            # if the key exists, then add the word to that key

            # if it doesnt exist, make it a key, and add the word to the value list for that key 


            # return all values

            # the whole 

            hm = {}

            for word in strs:
                chars_freq = [0] * 26

                for char in word: 
                    chars_freq[ord(char) - ord("a")] += 1
                
                if tuple(chars_freq) in hm:
                    hm[tuple(chars_freq)].append(word)
                else:
                    hm[tuple(chars_freq)] = [word]
            return list(hm.values())



            # hm = {}

            # for word in strs:
            #     chars_freq = set()

            #     for char in word: 
            #         chars_freq.add(char)
                
            #     if tuple(chars_freq) in hm:
            #         hm[tuple(chars_freq)].append(word)
            #     else:
            #         hm[tuple(chars_freq)] = [word]
            # return list(hm.values())
