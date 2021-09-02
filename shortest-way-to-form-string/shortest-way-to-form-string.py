class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        t = set(target)
        s = set(source)
        usource = ''
        for alpha in source:
            if alpha in t:
                usource += alpha
        for alpha in t:
            if alpha not in s:
                return -1
        result = 1
        i = 0
        for alpha in target:
            while usource[i]!=alpha:
                i += 1
                if i==len(usource):
                    i = 0
                    result += 1
            i += 1
            if i==len(usource):
                i = 0
                result += 1
        if i==0:
            result -= 1
        return result