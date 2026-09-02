class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        remainder_counts = {0: 1} # {sum: num of occurences of that sum}

        result = 0
        curr_sum = 0

        for i in range(len(nums)):

            curr_sum += nums[i]

            remainder = curr_sum - k

            if remainder in remainder_counts:
                result += remainder_counts[remainder]

           
            
            if curr_sum in remainder_counts:
                remainder_counts[curr_sum] += 1
            else: 
                remainder_counts[curr_sum] = 1
            
            

    
        

        return result








        