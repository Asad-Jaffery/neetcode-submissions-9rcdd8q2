class Solution:
    def rob(self, nums: List[int]) -> int:
        # max_of_n-2, max_of_n-1, n, n + 1
        # max_of_n = max((n + max_of_n-2), max_of_n-1)
        
        def max_robbed(nums):
            if len(nums) < 3: 
                return max(nums)

            max1 = nums[0]
            max2 = max(nums[0], nums[1])
            robbed = 0

            for n in nums[2:]:
                robbed = max((n + max1), max2)
                max1 = max2
                max2 = robbed
            return robbed
        
        if len(nums) > 1: 
            return max(max_robbed(nums[1:]), max_robbed(nums[:-1]))
        else: 
            return nums[0]





        