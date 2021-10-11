# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0
        return self.height(root)[1]
    
    def height(self, cur):
        if not cur:
            return (0,0)
        l, ls = self.height(cur.left)
        r, rs = self.height(cur.right)
        return (1+max(l, r), max([l+r, ls, rs]))