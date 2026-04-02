class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l, r = 0, len(heights) - 1

        while l < r:
            max_water = max(max_water, (min(heights[l], heights[r]) * (r - l)))
            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1
        return max_water



        # min(left, right) x right - left


        # how do we know when to increment the left pointer


        #  Can you think why we only move the pointer at smaller height?








    
           


        





        