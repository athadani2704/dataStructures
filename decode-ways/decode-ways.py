import string

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=="0":
            return 0
        elif len(s)==1:
            return 1
        result = [1,0]
        for i in range(len(s)-2, -1, -1):
            a, b = result
            if s[i]=="0":
                if s[i+1]=="0":
                    return 0
                continue
            cur = [0,0]
            if s[i+1]!="0":
                cur[0] += a+b
                if int(s[i:i+2])<=26 and a>0:
                    cur[1] = a
            elif int(s[i:i+2])<=26:
                cur = [0,a+b]
            else:
                return 0
            result = cur[:]
        return sum(result)
        
# - set alpha to dictionary containing mapping of digits to alphabets
# - set pointer i to second last index of s
# - set count to (1,0) if last index is greater than 0 otherwise (0,0) => (count when singly starting, count when doubly starting)
# - loop till i has not reach first index
#     - check if current element is >0
#     y=> - set current count to (0,0)
#         - check if next element is >0
#         y=> - increment current counts first value to sum of last elements pair (a,b)
#             - check if current element along with next one <=26 and last counts first val is >0
#             y=> - increment current counts second value by last elements first val a
#         n=> - check if current element along with next one >26
#             y=> - set current counts values to pair (0,0)
#                 - return 0
#             n=> - set current counts values to (0, a+b)
#         - update count to current counts pair (a',b')
# - return sum of pair elements of count
        
        