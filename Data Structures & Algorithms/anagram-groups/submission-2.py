class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a hash dict for quick look up to store each group of anagrams

        # the key should be the sorted anagram
        
        anagrams = {}
        for s in strs:
            sorted_string = "".join(sorted(s)) 
            if sorted_string in anagrams:
                anagrams[sorted_string].append(s)
            else: 
                anagrams[sorted_string] = [s]    
        
        return list(anagrams.values())