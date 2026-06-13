class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        al = "abcdefghijklmnopqrstuvwxyz"

        res = ""

        for word in words:
            total = 0

            for ch in word:
                total += weights[ord(ch) - ord('a')]

            total %= 26
            res += al[-(total + 1)]

        return res