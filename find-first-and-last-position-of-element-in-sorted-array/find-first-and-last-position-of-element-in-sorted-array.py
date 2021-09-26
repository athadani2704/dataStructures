class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0 or nums[0]>target or nums[-1]<target:
            return [-1,-1]
        if len(nums)==1:
            return [0,0] if nums[0]==target else [-1,-1]
        # search for starting
        start, end = 0, len(nums)-1
        si = ei = -1
        while start<end:
            mid = (start+end)//2
            if nums[mid]<target:
                start = mid+1
            elif nums[mid]>target:
                end = mid-1
            elif mid-1>=0 and nums[mid-1]==target:
                end = mid-1
            else:
                si = mid
                break
        if si==-1:
            if nums[start]!=target:
                return [-1, -1]
            else:
                si = start
        if (si+1<len(nums) and nums[si+1]>target) or si==len(nums)-1:
            return [si, si]
        # search for ending
        start, end = 0, len(nums)-1
        while start<end:
            mid = (start+end)//2
            if nums[mid]<target:
                start = mid+1
            elif nums[mid]>target:
                end = mid-1
            elif mid+1<len(nums) and nums[mid+1]==target:
                start = mid+1
            else:
                ei = mid
                break
        if ei==-1:
            ei = start
        return [si, ei]