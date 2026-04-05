class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        vertical = 0
        horizontal = 0 

        for direction in moves:
            match direction:
                case "D":
                    vertical -= 1
                case "U":
                    vertical += 1
                case "L":
                    horizontal -= 1
                case "R":
                    horizontal += 1
        
        return vertical == horizontal == 0