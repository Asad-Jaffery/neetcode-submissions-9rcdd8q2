class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        # for each number 
        # if number not in set of numbers we've done before

            # calculate target 
                # target: 0 - number
                # add this number to our set

            # check the other 2 numbers, see if they add to target
                # we do a double for loop (o(n^2))
                # OR 
            # add to a result list (of tuples)


        # convert all tuples to lists to return the result


        #  x    y   y  x  
        #[[-1, 0, 1], ]

        # if number is positive, l = 0, r = number
        # if num is negative, l = number + 1, r = len(nums) - 1
        # if num is 0, l = 0, r = len(nums) - 1



        # [-4, -1, -1, 0, 1, 2, 3]

        res = set()
        visited_nums = set() # -1 
        nums.sort()

        for i in range(len(nums)):
            if nums[i] not in visited_nums:
                visited_nums.add(nums[i])
                target = 0 - nums[i] # 1


                l, r = i + 1, len(nums) - 1
                # l = -1
                # r = 3
                while l < r:
                    current = nums[l] + nums[r]
                    if current == target: 
                        if (nums[i], nums[l], nums[r]) not in res:
                            res.add((nums[i], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif current < target:
                        l += 1
                    else:
                        r -= 1
        real_res = []
        for i in res:
            real_res.append(list(i))

        return real_res
                
                





        