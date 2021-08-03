# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rearrange(self, cur, curlen, l):
        if curlen==(l//2+1):
            return cur
        child = self.rearrange(cur.next, curlen+1, l)
        if (cur.next==child and not l%2) or cur==child:
            return child
        temp = cur.next
        cur.next = child.next
        temp1 = child.next.next
        child.next.next = temp
        child.next = temp1
        return child
        
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        cur = head
        l = 0
        while cur:
            l += 1
            cur = cur.next
        self.rearrange(head, 1, l)
        
        
# 1 2 3 4 5


# set cur to head
# if head or head.next does not exist then return
# set l to length of linked list
# call func with parameters cur.next and l+1 and l


# func(cur, curlen, l){
#     check if curlen is mid point+1 of l
#         if yes then
#             return cur
#     set child to func(cur.next, l+1, l)
#     if (cur.next = child and l is even) or cur=child then return child
#     else change directions and then return child
# }