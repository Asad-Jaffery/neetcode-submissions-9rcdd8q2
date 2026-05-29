class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # for each time where there is a profit, check to see if its max

        # if no profit, move the right pointer up 


        l, r = 0, 0
        profit = 0

        while r < len(prices):
            if prices[r] - prices[l] > 0:
                profit = max(profit, prices[r] - prices[l])
            else: 
                l = r
            r += 1
        print(l, r)
        return profit

        