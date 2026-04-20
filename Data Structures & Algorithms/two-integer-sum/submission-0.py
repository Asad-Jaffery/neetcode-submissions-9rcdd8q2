class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for each number in the array, there is a target we need to look for
        # goal = target - num[i]

        # for each number, we'll look for the target

        # set
        # dictionary --> 
            # number itself
            # index of that number
            # {number: index}

        visited = {}
        for i in range(len(nums)):
            goal = target - nums[i]

            if goal in visited:
                return [visited[goal], i]
            else:
                visited[nums[i]] = i
        



        