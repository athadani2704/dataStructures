# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==1:
            return TreeNode(preorder[0])
        return self.building(preorder, inorder, [0, len(preorder)-1], [0, len(inorder)-1])
    
    def building(self, preorder, inorder, pre_section, in_section):
        p1, p2, i1, i2 = pre_section[0], pre_section[1], in_section[0], in_section[1]
        if p1>p2:
            return None
        if p1==p2:
            return TreeNode(preorder[p1])
        left_section, right_section = [i1, inorder.index(preorder[p1])-1], [inorder.index(preorder[p1])+1, i2]
        left_pre, right_pre = [], []
        i = p1+1
        search_set = set(inorder[i1: left_section[1]+1])
        while i<=p2 and preorder[i] in search_set:
            i += 1
        left_pre = [p1+1, i-1]
        right_pre = [i, p2]            
        return TreeNode(preorder[p1], self.building(preorder, inorder, left_pre, left_section), self.building(preorder, inorder, right_pre, right_section))
        
        
# func(pre, ino, p1, p2, ino1, ino2){
#     check if ino1=ino2 and return ino[ino1] if yes
#     all nodes left of p1 in ino are left child and rest right child
#     pre.left = call func(pre, ino , indexes of pre that are in left section of ino, indexes of pre that are in right section of ino)
# }

# preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
#             i         j              a         b

# preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]        preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
#               i                      ab                                   i                        a    b

# return 9                                            preorder = [3,9,20,15,7], inorder = [9,3,15,20,7] preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
#                                                                         i                    ab                           i                        a b
                                                           