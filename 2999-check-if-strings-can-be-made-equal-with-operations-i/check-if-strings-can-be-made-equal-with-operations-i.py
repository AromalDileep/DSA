class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        
        return (
            sorted([s1[0], s1[2]]) == sorted([s2[2], s2[0]]) and
            sorted([s1[1], s1[3]]) == sorted([s2[3], s2[1]])
        )

            
                