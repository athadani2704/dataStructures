from math import inf

class MinStack:

    def __init__(self):
        self.stack = []
        self.freq = {}
        self.mn = inf

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mn = min(self.mn, val)
        self.freq[val] = self.freq.get(val, 0)+1

    def pop(self) -> None:
        self.freq[self.stack[-1]] -= 1
        if self.stack[-1]==self.mn and self.freq[self.stack[-1]]==0:
            self.mn = inf
            for k, v in self.freq.items():
                if v>0 and k<self.mn:
                    self.mn = min(self.mn, k)
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mn


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()