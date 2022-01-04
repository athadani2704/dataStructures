class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target>nums[-1]:
            return len(nums)
        elif target<nums[0]:
            return 0
        start, end = 0, len(nums)-1
        while start<end-1:
            mid = (start+end)//2
            if nums[mid]<target:
                start = mid
            elif nums[mid]>target:
                end = mid
            else:
                return mid
        return start+1 if nums[start]<target else start