class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vr1, vr2 = version1.split("."), version2.split(".")
        m, n = len(vr1), len(vr2)

        for i in range(max(m, n)): 
            v1 = int(vr1[i]) if i < m else 0 
            v2 = int(vr2[i]) if i < n else 0 

            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

        return 0