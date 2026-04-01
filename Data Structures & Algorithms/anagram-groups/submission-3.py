class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict with key -> set
        #    -> lisst of words

        anagrams = [] # list of anagram sets
        grouped_words = [] # list of list of words

        for word in strs: 
            sorted_word = sorted(word)
            if sorted_word in anagrams:
                index = anagrams.index(sorted_word)
                grouped_words[index].append(word)
            else: 
                anagrams.append(sorted_word)
                grouped_words.append([word])

        return grouped_words


        