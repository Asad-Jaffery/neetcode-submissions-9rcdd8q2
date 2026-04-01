class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy
        # sell

        # profit = sell - buy

        # if the buy is greater than the sell day, then increment the buy day (or both)?

        # if the sell day is greater than the buy day, then increment the sell day to see if it

        # scenario 1: negative profit / no profit
            # increment buying price (or both)

        # scenario 2: positive profit
            # record profit if it's the max
            # increment the sell day
        
        profit = 0
        buy = 0
        sell = 1

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = max(profit, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return profit





        
        
        