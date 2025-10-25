class Solution:
    def totalMoney(self, n: int) -> int:
        if n == 1:
            return 1
        monday = 0
        res = []
        for i in range(1, n+1): 
            if i% 7 == 0: 
                res.append(7 + monday)
                monday += 1
            else:
                res.append(i % 7 + monday)
        print(res)
        return sum(res)
        
