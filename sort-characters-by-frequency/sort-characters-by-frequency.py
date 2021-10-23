from string import ascii_lowercase as l, ascii_uppercase as u, digits as d

class Solution:
    def frequencySort(self, s: str) -> str:
        f = [[x,0] for x in l+u+d]
        for x in s:
            if ord(x)<58:
                f[52+int(x)][1] += 1
            elif ord(x)<91:
                f[ord(x)-65+26][1] += 1
            else:
                f[ord(x)-97][1] += 1
        result = ""
        for x in sorted(f, key=lambda a:a[1], reverse=True):
            result += x[0]*x[1] if x[1] else ""
        return result