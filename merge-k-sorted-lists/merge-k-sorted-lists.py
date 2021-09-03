# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as h
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        combined = []
        maps = {}
        for i in range(len(lists)):
            cur = lists[i]
            while cur:
                combined.append(cur.val)
                maps[cur.val] = maps.get(cur.val, [])+[cur]
                n = cur.next
                cur.next = None
                cur = n
        if len(combined)==0:
            return None
        h.heapify(combined)
        head = cur = maps[h.heappop(combined)].pop()
        while len(combined):
            cur.next = maps[h.heappop(combined)].pop()
            cur = cur.next
        return head