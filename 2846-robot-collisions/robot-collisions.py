class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        robots = sorted([(positions[i], healths[i], directions[i], i) 
                         for i in range(len(positions))])
        
        stack = []  # indices of robots moving right
        health = healths[:]  # copy
        
        for pos, h, d, i in robots:
            if d == "R":
                stack.append(i)
            else:
                # fight with previous right-moving robots
                while stack and health[i] > 0:
                    j = stack[-1]
                    
                    if health[j] < health[i]:
                        stack.pop()
                        health[i] -= 1
                        health[j] = 0
                    elif health[j] > health[i]:
                        health[j] -= 1
                        health[i] = 0
                    else:
                        health[j] = 0
                        health[i] = 0
                        stack.pop()
                        break
        
        # collect survivors
        result = []
        for i in range(len(health)):
            if health[i] > 0:
                result.append(health[i])
        
        return result

