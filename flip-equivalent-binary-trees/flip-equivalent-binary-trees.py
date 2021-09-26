# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        q1, q2 = Queue(), Queue()
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val!=root2.val:
            return False
        q1.put(root1)
        q2.put(root2)
        while not q1.empty() and not q2.empty():
            q1size, q2size = q1.qsize(), q2.qsize()
            if q1size!=q2size:
                return False
            for i in range(q1size):
                cur1, cur2 = q1.get(), q2.get()
                if ((cur1.left is not None)+(cur1.right is not None))!=((cur2.left is not None)+(cur2.right is not None)):
                    return False
                l1, r1, l2, r2 = -1, -1, -1, -1
                if cur1.left:
                    l1 = cur1.left.val
                    q1.put(cur1.left)
                if cur1.right:
                    r1 = cur1.right.val
                    q1.put(cur1.right)
                if cur2.left:
                    l2 = cur2.left.val
                if cur2.right:
                    r2 = cur2.right.val
                if l2 not in [l1, r1] or r2 not in [l1, r1]:
                    return False
                first = second = None
                if l2>=0:
                    if l2==l1:
                        first = cur2.left
                    else:
                        second = cur2.left
                if r2>=0:
                    if r2==r1:
                        second = cur2.right
                    else:
                        first = cur2.right
                if first:
                    q2.put(first)
                if second:
                    q2.put(second)
        return True