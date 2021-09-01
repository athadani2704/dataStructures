class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target<matrix[0][0] or target>matrix[-1][-1]:
            return False
        return self.findSolution(matrix, target)
    
    def findSolution(self, arr, target):
        # Search height
        start, end = 0, len(arr)-1
        while start<end-1:
            mid = (start+end)//2
            if arr[mid][0]>target:
                end = mid
            else:
                start = mid
        if target==arr[end][0]:
            return True
        elif target>arr[end][0]:
            row = end
        else:
            row = start
        start, end = 0, len(arr[0])-1
        while start<end:
            mid = (start+end)//2
            if arr[row][mid]<target:
                start = mid+1
            elif arr[row][mid]>target:
                end = mid-1
            else:
                return True
        return arr[row][start]==target