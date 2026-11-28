class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search 
        # we can use a left and right pointer,
            # compare mindpoint of the pointers to the target 
                # if the midpoint < target: leftpointer = m + 1
                # else rightpointer = m - 1

        # as long as l is less than r 

        l, r = 0, len(nums) - 1
        m = (l + r) // 2

        while l <= r: 
            if nums[m] == target: 
                return m
            elif nums[m] < target: 
                l = m + 1
            else: 
                r = m - 1
            m = (l + r) // 2

        return -1



        