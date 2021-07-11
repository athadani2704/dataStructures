class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None
    
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None
        self.median = None
        self.length = 0
        
    def addNum(self, num: int) -> None:
        if not self.head:
            self.head = Node(num)
            self.median = self.head
            self.length += 1
            return
        self.length += 1
        if self.head.val>=num:
            cur = Node(num)
            cur.next = self.head
            self.head.prev = cur
            self.head = cur
            if not self.length%2:
                self.median = self.median.prev
            return
        if num<=self.median.val:
            par = self.head
            cur = self.head.next
        else:
            par = self.median
            cur = self.median.next
        while cur and cur.val<num:
            par = cur
            cur = cur.next
        if not cur:
            par.next = Node(num)
            par.next.prev = par
            if self.length%2:
                self.median = self.median.next
            return
        else:
            par.next = Node(num)
            par.next.prev = par
            par.next.next = cur
            cur.prev = par.next
        if num<=self.median.val and not self.length%2:
            self.median = self.median.prev
        if num>self.median.val and self.length%2:
            self.median = self.median.next

    def findMedian(self) -> float:
        if self.length==0:
            return 0
        return self.median.val if self.length%2 else round((self.median.val+self.median.next.val)/2, 5)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()