class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        if len(prices)==2:
            return 0 if prices[1]<=prices[0] else prices[1]-prices[0]
        arr = [0 for i in range(len(prices))]
        arr[-2] = 0 if prices[-1]<=prices[-2] else prices[-1]-prices[-2]
        for i in range(len(prices)-3, -1, -1):
            curmax = arr[i+1]
            for j in range(i+1, len(prices)):
                if prices[j]>prices[i]:
                    curmax = max(curmax, prices[j]-prices[i]+(arr[j+2] if j+2<len(prices) else 0))
            arr[i] = curmax
        return arr[0]