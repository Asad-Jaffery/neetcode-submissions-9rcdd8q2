class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # height x width of the box
        # height = min (2 sides)

        # width = abs(left - right side)


        # l = 0, r = 1


        # while r < max
        # which one is smaller 

            # if the right side is smaller (or the same), we increment it by 1 

            # if the left side is smaller. we increment by 1, AND if left = right, we increase right by 1 again


        l, r = 0, len(heights) - 1
        area = 0

        while l < r:
            area = max(area, (min(heights[l], heights[r]) * (r - l)))

            if heights[r] <= heights[l]:
                r -= 1
            else: 
                l += 1
        
        return area