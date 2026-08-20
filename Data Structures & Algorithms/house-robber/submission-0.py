class Solution:
    def rob(self, nums: List[int]) -> int:

        # dp array
        # loop through nums
            # at each point, i choose max of (rob[i], don't rob i )

                        # rob[i] = dp[i-2] + nums[i]
                        # don't rob i = dp[i-1]

        dp = []
        dp.append(nums[0])

        if len(nums) > 1:
            dp.append(max(nums[0], nums[1]))

        for i in range(2, len(nums)):
            best_val = max((dp[i-2] + nums[i]), dp[i-1])
            dp.append(best_val)
        
        return max(dp)

