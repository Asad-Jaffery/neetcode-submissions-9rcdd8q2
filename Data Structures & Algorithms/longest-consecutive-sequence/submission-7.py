class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest_seq = 0

        for num in nums:
            if num - 1 not in numsSet:
                seq_len = 1
                curr_num = num
                while curr_num + 1 in numsSet:
                    curr_num += 1
                    seq_len += 1
                longest_seq = max(longest_seq, seq_len)
        
        return longest_seq
                

        
        










        