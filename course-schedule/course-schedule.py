class Solution:
    def findLowestWtKey(self, w):
        for key, val in w.items():
            if not val:
                return key
        return -1
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        v = {i:[] for i in range(numCourses)}
        weight = {i:0 for i in range(numCourses)}
        for pre in prerequisites:
            weight[pre[0]] += 1
            v[pre[1]].append(pre[0])
        # print(v, weight)
        for i in range(numCourses):
            lowest_wt = self.findLowestWtKey(weight)
            if lowest_wt==-1:
                return False
            for val in v[lowest_wt]:
                weight[val] -= 1
            weight.pop(lowest_wt)
        return True