# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return True if root.val==targetSum else False
        q = Queue()
        q.put(root)
        while not q.empty():
            cursize = q.qsize()
            for _ in range(cursize):
                cur = q.get()
                if not cur.left and not cur.right and cur.val==targetSum:
                    return True
                if cur.left:
                    cur.left.val += cur.val
                    q.put(cur.left)
                if cur.right:
                    cur.right.val += cur.val
                    q.put(cur.right)
        return False