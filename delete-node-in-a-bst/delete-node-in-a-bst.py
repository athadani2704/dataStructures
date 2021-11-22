# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        par = cur = root
        if not root:
            return None
        if not root.left and not root.right:
            return None if root.val==key else root
        par, node, pre, post = self.findNodeAndReplacement(key, root)
        if not node:
            return root
        if not pre and not post:
            if par.left==node:
                par.left = None
            else:
                par.right = None
            return root
        if pre:
            if pre==node:
                node.val = node.left.val
                node.left = node.left.left
            else:
                node.val = pre.right.val
                pre.right = pre.right.left
        else:
            if post==node:
                node.val = node.right.val
                node.right = node.right.right
            else:
                node.val = post.left.val
                post.left = post.left.right
        return root
        
    def findNodeAndReplacement(self, key, root):
        reqNode = None
        par = root
        while root and root.val!=key:
            par = root
            if root.val<key:
                root = root.right
            else:
                root = root.left
        if not root:
            return par, None, None, None
        else:
            reqNode = root
        if root.left:
            if not root.left.right:
                return par, reqNode, root, None
            root = root.left
            while root.right.right:
                root = root.right
            return par, reqNode, root, None
        elif root.right:
            if not root.right.left:
                return par, reqNode, None, root
            root = root.right
            while root.left.left:
                root = root.left
            return par, reqNode, None, root
        else:
            return par, reqNode, None, None