"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        if not head.next and not head.child:
            return head
        dummy = Node(0, None, None, head)
        cur, stack = head, [dummy]
        while len(stack):
            if cur.child:
                stack.append(cur)
                cur = cur.child
            elif cur.next:
                cur = cur.next
            else:
                if len(stack):
                    parent = stack.pop()
                    cur.next = parent.next
                    parent.next = parent.child
                    parent.child = None
                    parent.next.prev = parent
                    if cur.next:
                        cur.next.prev = cur
                cur = cur.next if cur.next else cur
        head.prev = None
        return head
        
    
# - set cur = head
# - set stack = []
# - loop thru till cur exists
#     - check if cur.child exists
#         - add cur to stack
#         - set cur to cur.child
#     - otherwise check if cur.next exists
#         - move cur to cur.next
#     - otherwise
#         - parent = pop last element from stack
#         - point cur.next to parent.next
#         - point parent.next to parent.child
#         - point parent.child to null
#         - point parent.next.prev to parent
#         - check if cur.next exists
#             - point cur.next.prev to cur
#         - move cur to cur.next
# - return head