class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}
        for s in strs:
            sorted_string = "".join(sorted(s)) # sort the string as another string
            if sorted_string in anagrams:
                anagrams[sorted_string].append(s)
            else: 
                anagrams[sorted_string] = [s]    
        
        return list(anagrams.values())