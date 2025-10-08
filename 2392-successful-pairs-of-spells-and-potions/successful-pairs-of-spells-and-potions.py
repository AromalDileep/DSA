import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        res = []

        for s in spells:
            # find the smallest potion >= success / s
            threshold = (success + s - 1) // s   # ceil division to avoid floating point --> bascially it is successs / s. It is just a mathematical trick
            j = bisect.bisect_left(potions, threshold)
            res.append(m - j)
        return res
