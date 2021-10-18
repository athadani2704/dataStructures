# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = Queue()
        if root.val in [x, y]:
            return False
        q.put((None, root))
        a, b = (-1, None), (-1, None)
        level = -1
        while not q.empty():
            level += 1
            for _ in range(q.qsize()):
                par, cur = q.get()
                if cur.val==x:
                    a = (level, par)
                elif cur.val==y:
                    b = (level, par)
                if a[0]>-1 and b[0]>-1:
                    return True if a[0]==b[0] and a[1] is not b[1] else False
                if cur.left:
                    q.put((cur, cur.left))
                if cur.right:
                    q.put((cur, cur.right))
        return False