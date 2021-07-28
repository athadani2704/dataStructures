# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        if not head.next:
            return None
        for i in range(n-1):
            cur = cur.next
            if not cur:
                return head
        prev = ListNode(0, head)
        p = prev
        while cur.next:
                prev = prev.next
                cur = cur.next
        prev.next = prev.next.next
        return p.next