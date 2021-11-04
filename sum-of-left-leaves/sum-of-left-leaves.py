# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q = Queue()
        q.put(root)
        result = 0
        while not q.empty():
            cursize = q.qsize()
            for _ in range(cursize):
                cur = q.get()
                if cur.left and not cur.left.left and not cur.left.right:
                    result += cur.left.val
                if cur.left:
                    q.put(cur.left)
                if cur.right:
                    q.put(cur.right)
        return result