class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        looked_at = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in looked_at:
                return [looked_at[diff], i]

            else:
                looked_at[nums[i]] = i
            
        