class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = {}
        for i, val in enumerate(s):
            if val not in pos:
                pos[val] = [i, i]
            else:
                pos[val][1] = i
        merge = sorted(pos.values(), key=lambda x:x[0])
        if len(merge)==1:
            return len(s)
        result = []
        for i in range(len(merge)-1):
            s1, e1, s2, e2 = merge[i][0], merge[i][1], merge[i+1][0], merge[i+1][1]
            if e1<s2:
                result.append(e1-s1+1)
                continue
            else:
                merge[i+1] = [s1, max(e1, e2)]
        result.append(merge[-1][1]-merge[-1][0]+1)
        return result
    
