class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        for val in nums:
            prod *= val if val!=0 else 1
        result = []
        if 0 in nums:
            if nums.count(0)>1:
                return [0]*len(nums)
            else:
                for val in nums:
                    result.append(0 if val!=0 else prod)
                return result
        const = -1 if prod<0 else 1
        for val in nums:
            result.append(self.divide(abs(prod), abs(val))*(-1 if val<0 else 1)*const)
        return result
    
    def divide(self, prod, val):
        if val==1:
            return prod
        start, end = 1, prod
        while start<end:
            mid = (start+end)//2
            if val*mid>prod:
                end = mid-1
            elif val*mid<prod:
                start = mid+1
            else:
                return mid
        return start