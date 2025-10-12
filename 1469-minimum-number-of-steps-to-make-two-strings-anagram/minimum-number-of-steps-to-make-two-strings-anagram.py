class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        count = 0

        # Count the extra characters in s that are not balanced by t
        for char in s_count:
            if s_count[char] > t_count.get(char, 0):
                count += s_count[char] - t_count.get(char, 0)

        return count
