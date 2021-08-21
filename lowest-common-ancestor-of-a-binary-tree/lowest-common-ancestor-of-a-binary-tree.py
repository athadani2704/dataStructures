# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in [p, q]:
            return root
        path = {p: None, q: None}
        if root.left:
            self.findCommon(root.left, p, q, path, [root]+[root.left])
        if root.right:
            self.findCommon(root.right, p, q, path, [root]+[root.right])
        i = 0
        while i<len(path[p]) and i<len(path[q]) and path[p][i]==path[q][i]:
            i += 1
        return path[p][i-1]
    
    def findCommon(self, cur, p, q, path, cur_path):
        if cur in [p, q]:
            path[cur] = cur_path
        if path[p] and path[q]:
            return
        if cur.left:
            self.findCommon(cur.left, p, q, path, cur_path+[cur.left])
        if cur.right:
            self.findCommon(cur.right, p, q, path, cur_path+[cur.right])