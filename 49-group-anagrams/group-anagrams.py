class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        out = defaultdict(list)

        for st in strs:
            count = [0] * 26
            for c in st:
                count[ord(c) - ord('s')] += 1
            
            out[tuple(count)].append(st)
        
        return list(out.values())