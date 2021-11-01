class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if not k:
            return
        temp = nums[-k:]
        for i in range(len(nums)-k-1, -1, -1):
            nums[i+k] = nums[i]
        for i in range(k):
            nums[i] = temp[i]