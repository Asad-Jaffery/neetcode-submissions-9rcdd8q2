class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            temp = 1
            for j in range(0, i):
                temp *= nums[j]
            for j in range(i + 1, len(nums)):
                temp *= nums[j]
            res.append(temp)
        return res

