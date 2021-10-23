class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return min(nums)
        elif nums[0]<nums[-1] or (nums[0]==nums[-1] and len(set(nums))==1):
            return nums[0]
        return self.findSolution(nums, 0, len(nums)-1)
    
    def findSolution(self, nums, start, end):
        mid = 0
        while start<end-1:
            mid = (start+end)//2
            if nums[mid]<nums[start]:
                end = mid
            elif nums[mid]>nums[start]:
                start = mid
            else:
                break
        if start<end-1:
            return min(self.findSolution(nums, start, mid), self.findSolution(nums, mid, end))
        else:
            return min(nums[start], nums[end])