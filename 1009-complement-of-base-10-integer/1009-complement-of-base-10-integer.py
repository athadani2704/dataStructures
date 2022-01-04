class Solution:
    def bitwiseComplement(self, n: int) -> int:
        x = 0
        while x<n:
            x = (x<<1)+1
        return x^n if n>0 else abs(n-1)