class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hm = {}
        words = s.split()

        # ✅ Important length check
        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in hm:
                # prevent two letters mapping to the same word
                if words[i] in hm.values():
                    return False
                hm[pattern[i]] = words[i]
            else:
                # check if existing mapping matches
                if words[i] != hm[pattern[i]]:
                    return False

        return True
