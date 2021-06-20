class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        result = 0
        if len(prices)==1:
            return 0
        for i, price in enumerate(prices, 1):
            if price<=min_so_far:
                min_so_far = price
                continue
            if price-min_so_far>result:
                result = price-min_so_far
        return result