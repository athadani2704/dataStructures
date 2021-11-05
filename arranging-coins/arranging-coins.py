from math import sqrt

class Solution:
    def arrangeCoins(self, n: int) -> int:
        s = int(sqrt(2*n))
        if s*(s+1)<=(2*n):
            return s
        else:
            return s-1