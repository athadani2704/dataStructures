# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        result = []
        to_delete = set(to_delete)
        if not root:
            return []
        self.findSolution(root, result, to_delete, True, True if root.val in to_delete else False)
        return result
    
    def findSolution(self, cur, result, to_delete, isrequired, isremove):
        left, right = cur.left, cur.right
        if isremove or (cur.left and cur.left.val in to_delete):
            if cur.left:
                cur.left = None
        if isremove or (cur.right and cur.right.val in to_delete):
            if cur.right:
                cur.right = None
        if not isremove and isrequired:
            result.append(cur)
        if left:
            self.findSolution(left, result, to_delete, True if isremove and left.val not in to_delete else False, True if left.val in to_delete else False)
        if right:
            self.findSolution(right, result, to_delete, True if isremove and right.val not in to_delete else False, True if right.val in to_delete else False)