class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrays = {}
        subarrays[0] = 1
        res = 0
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]

            remainder = curr_sum - k

            if remainder in subarrays: 
                res += subarrays[remainder]
            
            if curr_sum in subarrays:
                subarrays[curr_sum] += 1
            else: 
                subarrays[curr_sum] = 1
            
        return res









        
        