class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # binary search
        # check if the number is greater than equal to, or less than half
        # greater than, l = halfway
        # less than r = halfway

        # equal to, return the number 

        while l <= r:
            middle = (l + r) // 2
            if nums[middle] == target:
                return middle
            elif target < nums[middle]:
                r = middle - 1
            else: 
                l = middle + 1
        return -1

        lr   
[-1,0,2,4,6,8]

        


        

        