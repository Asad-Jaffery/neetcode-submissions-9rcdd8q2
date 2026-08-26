class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # compute subarry and keep track of the amount of subarrays of each as we go on 

        # sum[indeces we are exploring] - k = sum of subarray
            # if that exists, then we should get all of its values and add to the res 



        subarrays = {}
        subarrays[0] = 1

        res = 0
        curr = 0

        for i in range(len(nums)):
            curr += nums[i]
            remainder = curr - k

            if remainder in subarrays: 
                res += subarrays[remainder]
            
            if curr in subarrays: 
                subarrays[curr] += 1
            else: 
                subarrays[curr] = 1
        
        return res

            



        