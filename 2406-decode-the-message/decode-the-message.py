class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        u_key = ""
        seen = set()
        for i in range(len(key)):
            if key[i] in seen or key[i] == " ":
                continue
            u_key += key[i]
            seen.add(key[i])

        i_key = {u_key[i] : i+1 for i in range(len(u_key)) } 

        alphas = { i+1 : chr(ord('a') + i) for i in range(26)}
        res = ""

        for ch in message:
            if ch == " ":
                res += " "
            else:
                res += alphas[i_key[ch]] 
        return res

            