class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        dx, dy = 0, 1
        c = 0
        while True:
            for val in instructions:
                if val=="G":
                    x += dx
                    y += dy
                else:
                    dx, dy = self.updateDirection(val, dx, dy)
            if c==100:
                return False
            else:
                c += 1
            if (x, y)==(0, 0) and (dx, dy)==(0, 1):
                return True
        return False
    
    def updateDirection(self, val, dx, dy):
        if val=="L":
            if (dx, dy)==(0, 1):
                return -1, 0
            elif (dx, dy)==(-1, 0):
                return 0, -1
            elif (dx, dy)==(0, -1):
                return 1, 0
            else:
                return 0, 1
        else:
            if (dx, dy)==(0, 1):
                return 1, 0
            elif (dx, dy)==(1, 0):
                return 0, -1
            elif (dx, dy)==(0, -1):
                return -1, 0
            else:
                return 0, 1