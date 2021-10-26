import heapq as h
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums)==1:
            return 1
        minh, maxh = [nums[0]], [-nums[0]]
        h.heapify(minh)
        h.heapify(maxh)
        i, j = 0, 1
        freq = {nums[0]:1}
        result = 1
        A = nums
        while j<len(nums):
            i = self.updateWith(i, j, A, minh, 1, freq, maxh, limit)
            i = self.updateWith(i, j, A, maxh, -1, freq, minh, limit)
            h.heappush(minh, A[j])
            h.heappush(maxh, -A[j])
            freq[A[j]] = freq.get(A[j], 0)+1
            j += 1
            result = max(result, j-i)
        return result
            
    def updateWith(self, i, j, A, mmheap, multiplier, freq, otherheap, limit):
        while i<j and abs(A[j]-multiplier*mmheap[0])>limit:
            while mmheap[0]!=multiplier*A[i]:
                freq[A[i]] -= 1
                i += 1
            freq[A[i]] -= 1
            i += 1
            while len(mmheap) and freq[multiplier*mmheap[0]]==0:
                h.heappop(mmheap)
            while len(otherheap) and freq[multiplier*(-1)*otherheap[0]]==0:
                h.heappop(otherheap)
        return i
