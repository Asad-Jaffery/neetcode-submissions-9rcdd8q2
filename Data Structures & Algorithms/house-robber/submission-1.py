class Solution:
    def rob(self, nums: List[int]) -> int:
        max1, max2 = 0, 0
        # max1, max2, n, n + 1
       
        robbed = 0

        if len(nums) < 3: 
            return max(nums)
        else: 
            max1 = nums[0]
            max2 = max(nums[0], nums[1])
            for n in nums[2:]: 
                robbed = max((n + max1), max2)
                max1 = max2
                max2 = robbed
        return robbed



        

        