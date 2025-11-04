
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        n = len(nums)
        
        for i in range(n - k + 1):
            sub = nums[i:i+k]
            freq = Counter(sub)
            
            # Sort primarily by frequency descending, then by value descending
            sorted_items = sorted(freq.items(), key=lambda p: (-p[1], -p[0]))
            
            # Take the top x most frequent (or fewer if there are not enough)
            top_x_elements = {val for val, _ in sorted_items[:x]}
            
            # Calculate sum of subarray keeping only these top-x elements
            total = sum(num for num in sub if num in top_x_elements)
            res.append(total)
        
        return res
