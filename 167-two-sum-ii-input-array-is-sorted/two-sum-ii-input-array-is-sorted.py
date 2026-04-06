class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        def binary_search(left, right, target_val):
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == target_val:
                    return mid
                elif numbers[mid] < target_val:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        for i in range(len(numbers)):
            complement = target - numbers[i]
            
            j = binary_search(i + 1, len(numbers) - 1, complement)
            if j != -1:
                return [i + 1, j + 1]