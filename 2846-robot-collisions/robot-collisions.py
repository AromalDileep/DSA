class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        robots = sorted([(positions[i], healths[i], directions[i], i)
                        for i in range(len(positions))])
        
        stack = [] # storing right index
        health = healths[:] # copy 

        for pos, h, d, i in robots:
            if d == "R":
                stack.append(i)
            else:
                while stack and health[i] > 0:
                    j = stack[-1]
                    if health[j] > health[i]:
                        health[j] -= 1
                        health[i] = 0 
                    elif health[j] < health[i]:
                        health[j] = 0 
                        health[i] -= 1
                        stack.pop()
                    else:
                        health[j] = 0
                        health[i] = 0 
                        stack.pop()
        
        res = []
        for val in health:
            if val > 0:
                res.append(val)
        return res

