class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1

        while r < len(prices):
            curr_profit = prices[r] - prices[l]
            if curr_profit > 0:
                profit = max(profit, curr_profit)
            else: 
                l = r 
            r += 1

        return profit
                
        

