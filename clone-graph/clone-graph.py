"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from queue import Queue

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        if len(node.neighbors)==0:
            return Node(node.val)
        visited = set()
        added = set()
        copies = {}
        q = Queue()
        root = None
        q.put(node)
        added.add(node)
        while not q.empty():
            cur = q.get()
            visited.add(cur)
            added.remove(cur)
            if not root:
                root = Node(cur.val)
                copies[node] = root
            # print("par", cur.val)
            for neighbor in cur.neighbors:
                # print(neighbor.val)
                if neighbor not in visited and neighbor not in added:
                    q.put(neighbor)
                    added.add(neighbor)
                if neighbor not in copies:
                    copies[neighbor] = Node(neighbor.val)
                copies[cur].neighbors.append(copies[neighbor])     
        return root