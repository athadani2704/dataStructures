# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def updateTree(self, parent, child):
        if not child.left and not child.right:
            return 1 if child.val==1 else 0
        if child.left and self.updateTree(child, child.left)==0:
            child.left = None
        if child.right and self.updateTree(child, child.right)==0:
            child.right = None
        if child.left or child.right or child.val==1:
            return 1
        else:
            return 0
        
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root.left and not root.right:
            return root if root.val==1 else None
        if root.left and self.updateTree(root, root.left)==0:
            root.left = None
        if root.right and self.updateTree(root, root.right)==0:
            root.right = None
        return root if root.left or root.right or root.val==1 else None
    
    
# func(parent, child){
#     check if child is leaf node
#         if yes then check if child val = 1
#             if yes then return 1
#             else return 0
#     check if func(child, child.left)==0
#         if yes then break parents's connection with its left child
#     call func(child, child.right)==0
#         if yes then break parents's connection with its right child
#     check if atleast one child of parent exists or parent.val==1
#         if yes then return 1
#         else return 0
# }


# main(root){
#     check for root node being leaf node edge case
#     check if func(root, root.left)==0
#         if yes then return break root's connection with left child
#     check if func(root, root.right)==0
#         if yes then return break root's connection with right child
# }






