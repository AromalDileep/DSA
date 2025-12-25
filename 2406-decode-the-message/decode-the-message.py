class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}
        cur = 0
        
        for ch in key:
            if ch != " " and ch not in mapping:
                mapping[ch] = chr(ord('a') + cur)
                cur += 1

        res = []
        for ch in message:
            if ch == " ":
                res.append(" ")
            else:
                res.append(mapping[ch])
        
        return "".join(res)