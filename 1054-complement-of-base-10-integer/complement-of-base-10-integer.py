class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        res = ""
        for num in bin(n)[2:]:
            res += "1" if num == "0" else "0"
        
        return int(res, 2)