class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # binary search
        # check if the number is greater than equal to, or less than half
        # greater than, l = halfway
        # less than r = halfway

        # equal to, return the number 

        while l <= r:
            middle = (l + r) // 2 # without the parenthesis, this is an infinite loop!!!
            if nums[middle] == target:
                return middle
            elif target < nums[middle]:
                r = middle - 1
            else: 
                l = middle + 1
        return -1

        


        

        