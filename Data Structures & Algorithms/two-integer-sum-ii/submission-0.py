class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # the solution can not be past the index that is greater than the target int
        l, r = 0, len(numbers) - 1

        while numbers[l] + numbers[r] != target: 
            if numbers[l] + numbers[r] < target: 
                l += 1
            else:
                r -= 1

        
        return [l + 1, r + 1]
            



        