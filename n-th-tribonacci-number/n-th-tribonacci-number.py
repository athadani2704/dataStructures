class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=2:
            return 0 if n==0 else 1
        result = [0 for i in range(n+1)]
        result[1] = result[2] = 1
        for i in range(3, n+1):
            result[i] = result[i-1]+result[i-2]+result[i-3]
        return result[-1]