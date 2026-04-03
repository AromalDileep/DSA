class Solution:
    def frequencySort(self, s: str) -> str:
        
        count = Counter(s)

        s_count = sorted(count.items(), key=lambda x:x[1], reverse=True)

        res = ""

        for c, freq in s_count:
            res += c * freq 
        
        return res