class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # (r - l) * min(l, r)
            # r and l are 1 based index

        waters = set()

        l, r = 1, len(heights)

        while l < r:
            leftHeight = heights[l - 1]
            rightHeight = heights[r - 1]
            container_size = (r - l) * min(leftHeight, rightHeight)

            waters.add(container_size)

            if leftHeight <= rightHeight:
                l += 1
            else: 
                r -= 1
        
        
        return max(waters)




    
           


        





        