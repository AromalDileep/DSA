class Solution:
    def bestClosingTime(self, customers: str) -> int:
        score = len(customers)
        best = score
        hour = 0

        for i, c in enumerate(customers):
            score += 1 if c == 'Y' else -1
            if score > best:
                best = score
                hour = i + 1

        return hour
        