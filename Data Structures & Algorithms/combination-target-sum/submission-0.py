class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i, subset):
            if sum(subset) > target or i >= len(nums):
                return

            if sum(subset) == target:
                result.append(subset.copy())
                return

            #we will explore i again 
            subset.append(nums[i])
            dfs(i, subset)
            subset.pop()

            #we will explore i + 1 
            dfs(i + 1, subset)
        
        dfs(0, subset)
        return result





    


        