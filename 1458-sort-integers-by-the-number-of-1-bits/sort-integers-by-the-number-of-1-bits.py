from collections import defaultdict

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # 1. Group numbers by bit count
        h = defaultdict(list)
        for num in arr:
            h[num.bit_count()].append(num) 
        
        res = []
        for count in sorted(h.keys()):
            current_list = sorted(h[count])
            res.extend(current_list)
            
        return res