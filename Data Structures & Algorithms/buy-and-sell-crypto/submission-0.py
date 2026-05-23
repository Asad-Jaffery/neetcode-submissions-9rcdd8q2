class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l pointerr, r pointer
        # profit = r - l pointers 
        
        
        # we only consider new answer when there is a profit to be made
        # increase right pointer every time 
            # if there is NOT a profit, we set the left pointer to the right pointer? 


        # we do this until the right pointer reaches the end of the array

        profit = 0
        l, r = 0, 0

        while r <= len(prices) - 1:
            if prices[r] > prices[l]: # there is a potential new profit
                profit = max(profit, prices[r] - prices[l])
            else: 
                l = r
            r += 1
        return profit 

        