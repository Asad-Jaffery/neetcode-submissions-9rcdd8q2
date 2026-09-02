class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        # store results in a tuple in a set

        # iterate through the array - at each point
            # at each point, we do a two sum with the target being 0 - curr_num 

            # if l passes r, then no solution 
            # make sure that l and r are not i

        
        temp = set()
        for i in range(len(nums) - 2):
            target = 0 - nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == target: 
                    temp.add(tuple([nums[l], nums[r], nums[i]]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > target: 
                    r -= 1
                else: 
                    l += 1

                
        res = []
        for tup in temp: 
            res.append(list(tup))
        
        return res


                



        
        