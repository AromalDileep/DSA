class Solution:
    def minimumDistance(self, word: str) -> int:

        @cache
        def dp(si, f1, f2):

            if si == len(word):
                return 0
            
            c = word[si]
            pos = ord(c) - ord("A")
            i, j = pos//6, pos%6

            best = float("inf")

            distance1 = 0 if f1 == (-1,-1) else abs(f1[0]-i) + abs(f1[1]-j)
            best = min(best, distance1 + dp( si+1, (i, j), f2))
    
            distance2 = 0 if f2 == (-1,-1) else abs(f2[0]-i) + abs(f2[1]-j)
            best = min(best, distance2 + dp( si+1, f1, (i,j)))

            return best
        
        return dp(0, (-1,-1),(-1,-1))