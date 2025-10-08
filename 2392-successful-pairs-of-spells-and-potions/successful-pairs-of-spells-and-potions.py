class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        res = []

        for s in spells:
            l, r = 0, n - 1
            idx = n  # default = no valid potion

            # binary search for first potion that works
            while l <= r:
                mid = (l + r) // 2
                if s * potions[mid] >= success:
                    idx = mid      # possible valid index
                    r = mid - 1    # try to find smaller one
                else:
                    l = mid + 1

            res.append(n - idx)  # count of successful potions
        return res
