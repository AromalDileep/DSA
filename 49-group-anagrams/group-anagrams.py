class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        out = {}

        for st in strs:
            count = [0] * 26
            for c in st:
                count[ord(c) - ord('a')] += 1
            key = tuple(count) # compute once
            if key in out:
                out[key].append(st)
            else:
                out[key] = [st]
        return list(out.values())