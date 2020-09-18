class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        x, y = 0, 0
        curd = 0
        for i in instructions * 4:
            if i == "G":
                x += dirs[curd][0]
                y += dirs[curd % 4][1]
            elif i == "L":
                curd = (curd + 1) % 4
            elif i == "R":
                curd = (curd - 1) % 4
        return x == 0 and y == 0