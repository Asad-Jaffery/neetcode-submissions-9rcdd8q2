class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # how do i find the start of the sequence? 

        # number needs to have atleast 1 element that is possibly greater than it]

        nums_set = set(nums)
        res = 0
        curr_sequence = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in nums_set:
                curr_num = nums[i]
                curr_sequence = 1
                while curr_num + 1 in nums_set:
                    curr_sequence += 1
                    curr_num += 1
            res = max(res, curr_sequence)    
        return res








        