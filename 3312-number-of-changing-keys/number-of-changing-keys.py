class Solution:
    def countKeyChanges(self, s: str) -> int:
        count = 0 
        curr = s[0].lower()

        for i in range(1, len(s)):
            if s[i].lower() != curr:
                count += 1
                curr = s[i].lower()
        return count