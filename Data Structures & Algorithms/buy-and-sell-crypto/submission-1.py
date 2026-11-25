class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # exhaust all of the possible profit
        # once u get to a point with no proifit, make l = r 

        max_profit = buy = 0
        for sell in range(len(prices)):
            profit = prices[sell] - prices[buy]
            if profit > 0:
                max_profit = max(max_profit, profit)
            else: 
                buy = sell
        
        return max_profit



        