from typing import List

class Solution:
    def validateCoupons(
        self,
        code: List[str],
        businessLine: List[str],
        isActive: List[bool]
    ) -> List[str]:
        
        e, g, p, r = [], [], [], []

        valid_lines = {"electronics", "grocery", "pharmacy", "restaurant"}

        for i, active in enumerate(isActive):
            if not active:
                continue

            bl = businessLine[i]
            if bl not in valid_lines:
                continue

            if not code[i] or not all(c.isalnum() or c == '_' for c in code[i]):
                continue

            if bl[0] == 'e':e.append(code[i])
            elif bl[0] == 'g':g.append(code[i])
            elif bl[0] == 'p':p.append(code[i])
            elif bl[0] == 'r':r.append(code[i])

        return sorted(e) + sorted(g) + sorted(p) + sorted(r)
