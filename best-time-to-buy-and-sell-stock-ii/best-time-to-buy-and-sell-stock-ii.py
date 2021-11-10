from math import inf
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        prev = inf
        for price in prices:
            if price>prev:
                result += price-prev
            prev = price
        return result if result<inf else 0