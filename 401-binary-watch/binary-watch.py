class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8: return []
        # Hour = 5  → binary 0101 → 2 LEDs ON
        # Minute = 3 → binary 000011 → 2 LEDs ON
        # Total LEDs ON = 4
        ans = []

        for hour in range(12):
            for minute in range(60):
                if hour.bit_count() + minute.bit_count() == turnedOn:
                    ans.append(f"{hour}:{minute:02d}")
        return ans
                

