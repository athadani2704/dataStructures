# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left==right:
            return head
        dummy = ListNode(-1, head)
        prev, cur = dummy, head
        while left-1:
            prev = cur
            cur = cur.next
            right -= 1
            left -= 1
        pivotl = cur
        while right:
            curnext = cur.next
            cur.next = prev
            prev = cur
            cur = curnext
            right -= 1
        pivotl.next.next = prev
        pivotl.next = cur
        return dummy.next
        