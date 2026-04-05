class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        vertical = 0
        horizontal = 0 

        for direction in moves:
                if direction == "D": vertical -= 1
                elif direction == "U": vertical += 1
                elif direction == "L": horizontal -= 1
                elif direction == "R": horizontal += 1
        
        return vertical == horizontal == 0