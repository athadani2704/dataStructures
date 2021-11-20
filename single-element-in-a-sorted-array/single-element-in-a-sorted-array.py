class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        if len(nums)==1:
            return nums[0]
        elif nums[0]!=nums[1]:
            return nums[0]
        elif nums[-2]!=nums[-1]:
            return nums[-1]
        
        while start<end:
            mid = (start+end)//2
            if mid-1>=0 and nums[mid]!=nums[mid-1] and mid+1<len(nums) and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if mid%2==0:
                if nums[mid]==nums[mid+1]:
                    start = mid+1
                else:
                    end = mid-1
            else:
                if nums[mid]==nums[mid+1]:
                    end = mid-1
                else:
                    start = mid+1
        return nums[start]