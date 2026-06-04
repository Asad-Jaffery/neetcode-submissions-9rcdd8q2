class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if theres a profit, then see if max profit 

        # if not, sell left to the right pointer 

        profit = 0
        l, r = 0, 0
        while r < len(prices):
            if prices[r] - prices[l] > 0:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return profit 