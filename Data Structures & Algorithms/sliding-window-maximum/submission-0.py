class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        res = []
        while r < len(nums):
            currNums = []
            for i in range(l, r + 1):
                currNums.append(nums[i])
            res.append(max(currNums))
            l += 1
            r += 1
        
        return res


        