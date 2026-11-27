class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target - curr_num = what we're looking for

        # if what we're looking for is in a hashmap:
            # we found answer 

        # dict {num: index}

        hashmap = {}
        for i in range(len(nums)):
            possible_answer = target - nums[i]
            if possible_answer in hashmap:
                return [hashmap[possible_answer], i]
            hashmap[nums[i]] = i


        