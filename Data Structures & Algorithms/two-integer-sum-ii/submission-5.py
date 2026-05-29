class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # would have a small pointer (beginning of the array)
        # would have a large pointer (end of the arrray)

        # if the sum of the pointers > target
            # decrease large pointer 
        
         # if the sum of the pointers < target
            # increase small pointer 
        
        # return the two pointers if their sum == target 

        small, large = 0, len(numbers) - 1

        while small < large:
            if numbers[small] + numbers[large] == target:
                return [small + 1, large + 1]
            elif numbers[small] + numbers[large] < target:
                small += 1
            else:
                large -= 1
        

        


        
            
