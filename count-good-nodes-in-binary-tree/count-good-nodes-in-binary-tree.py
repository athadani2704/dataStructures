# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = Queue()
        q.put((root, root.val))
        if not root.left and not root.right:
            return 1
        result = 1
        while not q.empty():
            cur = q.get()
            if cur[0].left:
                result += (cur[1]<=cur[0].left.val)
                q.put((cur[0].left, max(cur[1], cur[0].left.val)))
            if cur[0].right:
                result += (cur[1]<=cur[0].right.val)
                q.put((cur[0].right, max(cur[1], cur[0].right.val)))
        return result