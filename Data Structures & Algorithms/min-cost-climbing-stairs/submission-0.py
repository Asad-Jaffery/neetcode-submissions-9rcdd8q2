class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # len(dp array) = len(cost) + 1

        # total cost of each point = cost at that point + min(dp[i] - 1, dp[i] - 2)


        total_costs = [0] * (len(cost) + 1)

        for i in range(len(total_costs)): # define first two as just the cost to leave that floor
            if i < 2: 
                total_costs[i] = cost[i]
            elif i == len(total_costs) - 1: # last element should just be the cost to get to that floor
                return min(total_costs[i - 1], total_costs[i - 2])
            else: # every other index should be cost to get to that floor + cost to leave that floor
                total_costs[i] = cost[i] + min(total_costs[i - 1], total_costs[i - 2]) 





        