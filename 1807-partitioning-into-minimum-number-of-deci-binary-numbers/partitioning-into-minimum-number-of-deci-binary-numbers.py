class Solution:
    def minPartitions(self, n: str) -> int:
        
        max_num = 0 
        for num in n:
            max_num = max(max_num, int(num))
            if max_num == 9:
                break
        
        return max_num