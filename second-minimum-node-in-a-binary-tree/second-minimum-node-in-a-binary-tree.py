# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root.left:
            return -1
        q = Queue()
        q.put(root)
        result = -1
        while not q.empty():
            l = q.qsize()
            # print(l)
            for i in range(l):
                cur = q.get()
                # print(cur.val)
                if cur.val!=root.val and (result==-1 or cur.val<result):
                    result = cur.val
                if cur.left:
                    q.put(cur.left)
                    q.put(cur.right)
        return result