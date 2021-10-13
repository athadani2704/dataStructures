# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.findSolution(preorder, 0, len(preorder))
    
    def findSolution(self, arr, start, end):
        if end-start<1:
            return None
        cur = TreeNode(arr[start])
        if end-start==1:
            return cur
        elif end-start==2:
            if arr[start+1]<arr[start]:
                cur.left = TreeNode(arr[start+1])
            else:
                cur.right = TreeNode(arr[start+1])
            return cur
        elif arr[start+1]>arr[start]:
            cur.right = self.findSolution(arr, start+1, end)
            return cur
        for i in range(end-1, start, -1):
            if arr[i]<arr[start]:
                cur.left = self.findSolution(arr, start+1, i+1)
                cur.right = self.findSolution(arr, i+1, end)
                break
        return cur
        
# func(arr){
#     -if arr len is 1 then return it as a node
#     -parse arr from last till all elements are greater than first element
#     -set left of current node as func(arr[left section])
#     -set right of current node as func(arr[right section])
# }