# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        root = ListNode(0, head)
        head = root
        cur = head
        if k==1:
            return head.next
        while cur:
            if not self.isRevPossible(cur, k):
                return head.next
            newHead, newTail, newCur = self.reverse(cur, cur.next, k)
            cur.next = newHead
            newCur.next = newTail
            cur = newCur
        return head.next
            
    def isRevPossible(self, cur, k):
        for i in range(k):
            cur = cur.next
            if not cur:
                return False
        return True
    
    def reverse(self, par, cur, k):
        head = cur
        for i in range(k):
            temp = cur.next
            cur.next = par
            par = cur
            cur = temp
        return (par, cur, head)