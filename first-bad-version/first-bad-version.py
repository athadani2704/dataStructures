# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
from math import inf
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = inf
        start, end = 1, n
        while start<end:
            mid = (start+end)//2
            if isBadVersion(mid):
                result = mid
                end = mid-1
            else:
                start = mid+1
        if start<result and isBadVersion(start):
            return start
        else:
            return result