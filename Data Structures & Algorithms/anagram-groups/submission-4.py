class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary 
        # {word: [anagrams]}

        # 2 options for keys
        
        # sort each word 
        
        # set
            # unique letters of each word
            # do not want to take this approach
                # in case there are multiple of the same char in a word
                # dont think we can have a set as a key in a dict 

        
        # check each word sorted to see if its in the dict already
            # if it is, then add the word to array value

            # if is is not, create the key, and add the word



        # dict : [aht: ["hat"],act: ["act", "cat"], askj: ["stop", "pots", "tops"]]

        # dict.values --> hopefully returns list of lists

        
        anagrams = {}

        for word in strs:
            sorted_word_list = sorted(word)

            sorted_word = ""
           
            for char in sorted_word_list:
                sorted_word += char

            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = []
                anagrams[sorted_word].append(word)

        print(anagrams.values())
        
        return list(anagrams.values())




        