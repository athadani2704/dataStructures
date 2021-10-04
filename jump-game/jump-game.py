class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0]==0:
            return True if len(nums)==1 else False
        is_zero = False
        for num in nums:
            if num==0:
                is_zero = True
                break
        if not is_zero:
            return True
        for i, num in enumerate(nums):
            if num or i==len(nums)-1:
                continue
            j = i-1
            while j>=0 and nums[j]<=i-j:
                j -= 1
            if j<0:
                return False
        return True