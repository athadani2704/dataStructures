class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s)==1:
            return 0
        elif len(s)==2:
            return 0 if '1' not in s or '0' not in s else 1
        i = 0
        newStr = ''
        while i<len(s):
            j = i+1
            while j<len(s) and s[j]==s[j-1]:
                j += 1
            newStr += str(j-i)+"_"
            i = j
        # print(newStr)
        result = 0
        newStr = newStr.split("_")
        for i in range(len(newStr)-2):
            result += min(int(newStr[i]), int(newStr[i+1]))
        return result