class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a dict to store the value : quantity 


        # for i in range (k) 
            # add the max value to the result 

            # delete that from the dict 

        quantities = {}

        for i in range(len(nums)):
            if nums[i] in quantities:
                quantities[nums[i]] += 1
            else:
                quantities[nums[i]] = 1

        res = []
        
        for i in range(k):
            key = max(quantities, key=quantities.get)
            res.append(key)
            del quantities[key]

        return res

       