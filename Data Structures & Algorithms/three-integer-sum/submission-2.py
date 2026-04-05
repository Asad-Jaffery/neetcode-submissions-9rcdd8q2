class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force: o(n^3)
            # for each number, check for each number two more times to find the combo that sum to 0
        # res = []
        # check = set()
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         for k in range(len(nums)):
        #             if i != j and j != k and i != k:
        #                 if nums[i] + nums[j] + nums[k] == 0:
        #                     curr_set = tuple(sorted([nums[i], nums[j], nums[k]]))
        #                     if curr_set not in check:
        #                         res.append([nums[i], nums[j], nums[k]])
        #                         check.add(curr_set)
                            
        # return res

        # for each number 
            # get a target number
            # do a two pointer to see if target num exists
                # if it does, add that lsit
                # if not, move to the next number in the outer foor loop

        nums.sort()
        checked = set()
        res = []
        for i in range(len(nums)):
            if nums[i] not in checked:
                checked.add(nums[i])

                target = 0 - nums[i]

                l, r = i + 1, len(nums) - 1

                while l < r:
                    if nums[l] + nums[r] == target:
                        res.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:  # skip l duplicates
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:  # skip r duplicates
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] < target:
                        l += 1
                    else: 
                        r -= 1
            
        return res
            
                       

            
                        


        

        