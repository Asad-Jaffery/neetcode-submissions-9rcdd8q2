class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = {}
        

        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word not in grouped_anagrams:
                grouped_anagrams[sorted_word] = []
            grouped_anagrams[sorted_word].append(word)

        return list(grouped_anagrams.values())


        