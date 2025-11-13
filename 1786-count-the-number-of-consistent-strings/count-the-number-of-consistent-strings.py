class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        counts = 0

        for w in words:
            if all(c in allowed_set for c in w):
                counts +=1

        return counts