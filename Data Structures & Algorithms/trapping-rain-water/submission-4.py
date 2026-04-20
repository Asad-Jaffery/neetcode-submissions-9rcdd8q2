class Solution:
    def trap(self, height: List[int]) -> int:

        # the left max will start at 0
        # if heights[i] > left, then re assign


        # the right max will start with the highest block
        # if heights[i] == right, recomputer max right with max(height[i:])

        left = []
        right = [0] * len(height)
        
    
        left.append(0)
        for i in range(1, len(height)):
            left.append(max(left[i-1], height[i-1]))
        
        right[len(height) - 1] = 0
        for i in range(len(height) - 2, 0, -1):
            right[i] = (max(right[i+1], height[i+1])) # this is wrong

        print(right)
        


        water_count = 0
        for i in range(len(height)):

            # reassign left and right
            left_max = left[i]
            right_max = right[i]

            water_to_add = min(left_max, right_max) - height[i]

            if water_to_add > 0:
                water_count += water_to_add
        
        return water_count


        