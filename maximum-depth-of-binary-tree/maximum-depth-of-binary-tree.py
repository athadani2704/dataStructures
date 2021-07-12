# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        q = Queue()
        level = 0
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        q.put(root)
        while not q.empty():
            cursize = q.qsize()
            level += 1
            for _ in range(cursize):
                cur = q.get()
                if cur.left:
                    q.put(cur.left)
                if cur.right:
                    q.put(cur.right)
        return level