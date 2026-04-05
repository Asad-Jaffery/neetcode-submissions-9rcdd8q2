class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # small pointer (l)
        # big pointer (r)
        # if sum is too large, then decrease big pointer
        # if sum is too small, then increase small pointer

        l, r = 0, len(numbers) - 1
        while l <= r:
            curr = numbers[l] + numbers[r]
            if curr == target:
                return [l + 1, r + 1]
            if curr < target:
                l += 1
            else:
                r -=1
        
            
