# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elif not head.next or not head.next.next:
            return head
        eve = head.next
        par, cur = head, head.next
        isodd = True
        while cur.next:
            par.next = cur.next
            par, cur = cur, cur.next
            isodd = not isodd
        if isodd:
            par.next = eve
        else:
            par.next = None
            cur.next = eve
        return head