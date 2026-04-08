class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # need to identify each of numbers who can be a valid starting point

        # only check for the sequences that come after those numbers

        numsSet = set(nums)
        res = 0
        if nums:
            res += 1

        for num in numsSet:
            if num - 1 not in numsSet:
                i = 1
                count = 1
                while num + i in numsSet:
                    count += 1
                    res = max(res, count)
                    i += 1
                
        return res

                

        
        










        