class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # get the frequency of each element

        # [] integers
        # [] frequencies of the integets

        # for i < k 
        # max frequency from the frequncies array
        # get the correstponding number in the integers array

        ints = []
        freq_of_ints = []
        ret = []


        for i in range(len(nums)):
            if nums[i] in ints:
                index = ints.index(nums[i]) # check syntax
                freq_of_ints[index] += 1
            else: 
                ints.append(nums[i])
                freq_of_ints.append(1)
        print(ints)
        print(freq_of_ints)
        
        for i in range(k):
            max_freq = max(freq_of_ints) # most frequent char

            index = freq_of_ints.index(max_freq) # get the index of most freq char | syntax
            top_k = ints[index] # get the corresponding index in ints
            ret.append(top_k) # add to return list

            del freq_of_ints[index] # remove 
            del ints[index] # remove
        
        return ret






