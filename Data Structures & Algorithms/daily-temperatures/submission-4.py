class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # for each temp in temparatures
            # start at index we're at --> compare temp to eahc next temp and keep track of how many it takes

        res = []
        for curr in range(len(temperatures)):
            days = 0
            future = curr
            while future <= len(temperatures) - 1 and temperatures[future] <= temperatures[curr]:
                future += 1
            if future <= len(temperatures) - 1:
                days = future - curr 
                res.append(days)
            else: 
                res.append(0)
        
        return res
            
 