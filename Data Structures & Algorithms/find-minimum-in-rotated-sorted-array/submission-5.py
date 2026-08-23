class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0, len(nums) - 1
        m = (l + r) // 2

        
        while l < r:

        
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[l]:
                r = m - 1
            elif nums[l] <= nums[m] <= nums[r]:
                return nums[l] 
            if nums[m - 1] > nums[m]:
                return nums[m]

            m = (l + r) // 2
        return nums[l]






        