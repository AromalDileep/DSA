class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        res = ""
        b = bin(n)[2:]
        for num in b:
            res += "1" if num == "0" else "0"
        
        return int(res, 2)