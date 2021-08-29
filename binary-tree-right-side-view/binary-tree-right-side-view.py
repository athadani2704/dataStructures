# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        q = Queue()
        q.put(root)
        result = []
        while not q.empty():
            size = q.qsize()
            for i in range(size):
                cur = q.get()
                if i==0:
                    result.append(cur.val)
                if cur.right:
                    q.put(cur.right)
                if cur.left:
                    q.put(cur.left)
        return result        