class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s) > k:
            result = ""

            cap = 0
            temp = 0

            for i in range(len(s)):
                temp += int(s[i])
                cap += 1

                if cap == k:
                    result += str(temp)
                    temp = 0
                    cap = 0

            if cap > 0:
                result += str(temp)

            s = result

        return s
