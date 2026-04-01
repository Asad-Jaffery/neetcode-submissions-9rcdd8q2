class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
    # while l != r or l < r
    # look at the middle
        # if the num is greater than the middle, then increase l to be the middle

        # if the num is less than the middle, then decrease r to be the middle
       
        while l <= r: # this needs to be equals to
            middle = (l + r) // 2
            if nums[middle] == target:
                return middle
                
            if target > nums[middle]:
                l = middle + 1 
            elif target < nums[middle]:
                r = middle - 1
        return -1







        