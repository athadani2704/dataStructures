# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.right or not root.left:
            return 1 if not root.right and not root.left else 2
        cur = root
        height = 0
        while cur.right:
            cur = cur.right
            height += 1
        nodes, isone = self.findLowest(root, 0, height, 0)
        if isone==-1:
            return 2**(height+1)-1
        else:
            return 2*(2**height-nodes+1)-isone+2**(height+1)-1
    
    def findLowest(self, cur, level, height, nodesAtHeight):
        if level==height:
            nodesAtHeight += 1
            if cur.right:
                return (nodesAtHeight, 0)
            elif cur.left:
                return (nodesAtHeight, 1)
            else:
                return (nodesAtHeight, -1)
        if cur.right:
            nodesAtHeight, isone = self.findLowest(cur.right, level+1, height, nodesAtHeight)
            if isone>-1:
                return (nodesAtHeight, isone)
        if cur.left:
            nodesAtHeight, isone = self.findLowest(cur.left, level+1, height, nodesAtHeight)
        return (nodesAtHeight, isone)
            
        