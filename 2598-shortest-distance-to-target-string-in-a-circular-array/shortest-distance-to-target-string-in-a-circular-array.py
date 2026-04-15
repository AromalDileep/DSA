class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        
        n = len(words)
        res = float("inf")

        for i in range(n):

            if words[(startIndex + i) %n] == target:
                res = min(res, i)
            
            if words[(startIndex -i) %n] == target:
                res = min(res, i)
        
        return res if res != float("inf") else -1
