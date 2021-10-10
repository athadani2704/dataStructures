from math import log

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left==0:
            return 0
        if left==right:
            return left
        sqLeft, sqRight = self.wholeSquareGreater(left), self.wholeSquareGreater(right)
        if sqLeft!=sqRight:
            return 0
        for val in range(left+1, right+1):
            left &= val
        return left
    
    def wholeSquareGreater(self, val):
        result = ceil(log(val, 2))
        return result+1 if result==log(val, 2) else result