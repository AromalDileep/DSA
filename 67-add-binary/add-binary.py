class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)
        res = a + b 
        print(res)
        print(bin(res)[2:])
        return bin(res)[2:]
        