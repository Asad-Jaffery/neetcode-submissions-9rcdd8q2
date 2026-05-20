class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # can not let l become greater than r
        # find the middle
        # if the target > m, l = m
        # if the target < m r = m

        # if target == m: 
            # return m

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return -1

    
        # [-1,0,2,4,6,8]
        # l = 2
        # r = 4
        # m = 4



