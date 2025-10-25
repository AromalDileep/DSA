class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7

        full_weeks = 28 * weeks + 7 * (weeks * (weeks - 1)) // 2
        remaining_days = days * (weeks + 1) + (days * (days - 1)) // 2
        return full_weeks + remaining_days
