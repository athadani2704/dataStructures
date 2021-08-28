# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        distance = {}
        self.updateDistance(root, distance, None, target)
        self.updateDistance(root, distance, None, target)
        result = []
        for key, v in distance.items():
            if v==k:
                result.append(key)
        return result
    
    def updateDistance(self, current, distance, parent, target):
        if current.val not in distance and current==target:
            distance[current.val] = 0
        if parent and parent.val in distance and current.val not in distance:
            distance[current.val] = distance[parent.val]+1
        if current.left:
            self.updateDistance(current.left, distance, current, target)
        if current.left and current.left.val in distance and current.val not in distance:
            distance[current.val] = distance[current.left.val]+1
        if current.right:
            self.updateDistance(current.right, distance, current, target)
        if current.right and current.right.val in distance and current.val not in distance:
            distance[current.val] = distance[current.right.val]+1
            