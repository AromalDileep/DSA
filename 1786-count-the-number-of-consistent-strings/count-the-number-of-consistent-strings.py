class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(list(allowed))
        words_set = list(map(set, words))

        counts = 0 
        for sets in words_set:
            counts += 1
            for char in sets:
                if char not in allowed_set:
                    counts -= 1
                    break
        return counts