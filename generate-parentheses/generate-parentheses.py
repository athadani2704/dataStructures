class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        on, off = n-1, n
        stack = [('(', n-1, n)]
        result = []
        while len(stack):
            curPath, on, off = stack.pop()
            if on==off:
                if on:
                    stack.append((curPath+'(', on-1, off))
                else:
                    result.append(curPath)
            else:
                if on:
                    stack.append((curPath+'(', on-1, off))
                if off:
                    stack.append((curPath+')', on, off-1))
        return result