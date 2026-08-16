class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # loop through the array, keep a count of each element via dict 
        
        # {1: 5, 6: 1, 5: 4} 


        # get array of values 
        # get array of numbers

        # when you select the max, you remove the top k - 1 elements, and return k 
            # how to get the index of the max? 
           #  numbers.index(max(numbers))

        res = []
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else: 
                counts[num] = 1
        
        keys = list(counts.keys()) # keys as an array
        values = list(counts.values()) # values as an array

        for i in range(k): 
            max_index = values.index(max(values))

            res.append(keys[max_index])

            values.pop(max_index) # remove the max element by it's index
            keys.pop(max_index) # remove the max element by it's index

        return res