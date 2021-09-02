class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k>=len(cardPoints):
            return sum(cardPoints)
        cursum = maxsum = sum(cardPoints[-k:])
        for i in range(k):
            cursum = cursum+cardPoints[i]-cardPoints[-k+i]
            maxsum = max(maxsum, cursum)
        return maxsum