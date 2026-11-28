class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # for each num in nums:

        # target = 0 - num

        # loop through the rest of the array via j, to see if target - j exists in the rest of the array 
            # we can do ths via a hashmap 

        # can store each result as a tuple in a set 
        
        # at the end return each tuple as a list

        # build the hashmap first
        hashmap = {}
        for i, n in enumerate(nums):
            hashmap[n] = i

        results = set()
        
        for i, i_num in enumerate(nums):
            target = 0 - i_num

            for j, j_num in enumerate(nums[i + 1:], start=i+1):
                third = target - j_num

                if third in hashmap and (hashmap[third] != i and hashmap[third] != j): 
                    pair = tuple(sorted((i_num, j_num, third)))
                    results.add(pair)
        
        string_results = []
        for r in results: 
            string_results.append(list(r))
        
        return string_results


