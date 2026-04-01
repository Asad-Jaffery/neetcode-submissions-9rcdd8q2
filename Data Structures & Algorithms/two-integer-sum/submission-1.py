class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}
        for i in range(len(nums)):
            if (target - nums[i]) in storage:
                return [storage[target - nums[i]], i]
            else: 
                storage[nums[i]] = i
        return None





        