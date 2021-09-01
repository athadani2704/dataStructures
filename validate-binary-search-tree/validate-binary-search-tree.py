# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        return self.isValid(root, -inf, inf)
    
    def isValid(self, root, lowest, highest):
        if not root:
            return True
        if root.val<=lowest or root.val>=highest:
            return False
        return self.isValid(root.left, lowest, root.val) and self.isValid(root.right, root.val, highest)