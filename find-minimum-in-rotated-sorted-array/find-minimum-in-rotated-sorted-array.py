class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return min(nums)
        if nums[0]<nums[-1]:
            return nums[0]
        start, end = 0, len(nums)-1
        while start<end:
            mid = (start+end)//2
            if nums[mid]>=nums[start] and nums[mid]>nums[end]:
                start = mid+1
            elif (nums[mid]<=nums[start] and nums[mid]<nums[end]) or (nums[mid]>=nums[start] and nums[mid]<nums[end]):
                end = mid
        return nums[start]
            