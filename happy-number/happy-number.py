class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        cache = set()
        while n not in cache:
            cache.add(n)
            x = 0
            for val in str(n):
                x += int(val)**2
            n = x
            if n==1:
                return True
        return False