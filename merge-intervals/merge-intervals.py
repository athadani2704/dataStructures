class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i, j = 0, 1
        result = []
        if len(intervals)==1:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        while j<len(intervals):
            if intervals[i][1]<intervals[j][0]:
                result.append(intervals[i])
                i = j
            elif intervals[i][1]<intervals[j][1]:
                intervals[i][1] = intervals[j][1]
            j += 1
        result.append(intervals[i])
        return result
    
# 1     3
#  2         6
#               8  10
#                     15   18

            
            
            
            
            
            
            
# sort by start
# repeat following till your comparison pointer reaches end of list
# check if start of next value is beyong e1
#     if yes then make this as an interval
#     if no then check if end of next value is beyond e1
#         if yes then update e1 with e2
#     irrespective move on to next value
# add last element interval to the result

# s1 e1 s2 e2
# s1 s2 e1 e2
# s1 s2 e2 e1
