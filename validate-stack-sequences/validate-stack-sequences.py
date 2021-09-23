from math import inf
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        push = set()
        for i in range(len(pushed)):
            if pushed[i]==0:
                pushed[i] = inf
            if popped[i]==0:
                popped[i] = inf
        i = 0
        for val in popped:
            if pushed[i]!=val and val in push:
                return False
            while i<len(pushed) and pushed[i]!=val:
                push.add(abs(pushed[i]))
                i += 1
            if pushed[i]==val:
                push.add(val)
                pushed[i] *= (-1)
                while i>=0 and pushed[i]<=0:
                    i -= 1
                i = 0 if i<0 else i
            else:
                return False
        return True
        
        
# - set i=0, push=empty set, j=0
# - loop through popped showing jth element{
#     - loop through push from i till len of push till pu[i]!=po[j]
#         - check if element is +ve
#             - if yes then check if value of element already in push set
#                 - if yes then return false
#             - add element to push set
#         - i++
#     - check if pu[i]==po[j]
#         - if yes then 
#             - update element to -ve value
#             - decrement i until you reach a +ve value or i<0
#         - otherwise return false
#     - j++
# }
# - return true
        
# [1,2,3,4,5]


# [1,2,3,4,5]
# [3,4,2,5,1]