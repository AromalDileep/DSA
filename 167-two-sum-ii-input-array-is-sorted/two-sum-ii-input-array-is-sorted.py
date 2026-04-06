class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            complement = target - numbers[i]
            
            j = bisect.bisect_left(numbers, complement, i+1)
            
            if j < len(numbers) and numbers[j]  == complement:
                return [i+1, j+1]