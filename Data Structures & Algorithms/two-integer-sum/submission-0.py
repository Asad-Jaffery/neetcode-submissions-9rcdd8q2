class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # {value: index}

        # get diff (target - curr_num), and see if its in the map
            # if yes, then return the pair

        # if not, then do not return anything


        explored = {}
        for i in range(len(nums)):
            if target - nums[i] in explored: 
                return [explored[target - nums[i]], i]
            explored[nums[i]] = i
        

        