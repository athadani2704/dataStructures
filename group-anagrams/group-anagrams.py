class Solution:
    def match(self, a, b):
        freq = {}
        for x in a:
            freq[x] = freq.get(x, 0)+1
        for x in b:
            if x not in freq or freq[x]==0:
                return False
            else:
                freq[x] -= 1
        return True
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqs = {}
        for st in strs:
            freqs[len(st)] = freqs.get(len(st), [])+[st]
        result = []
        for freq, vals in freqs.items():
            temp = []
            while len(vals)>0:
                flag = 0
                cur = vals.pop()
                for i in range(len(temp)):
                    if self.match(temp[i][0], cur):
                        temp[i].append(cur)
                        flag = 1
                        break
                if len(temp)==0 or flag==0:
                    temp.append([cur])
            result.extend(temp)
        return result
                
        
        
        
# strs = ["eat","tea","tan","ate","nat","bat"]

# 3: {e:1, a:1, t:1}, {}
# dict = {}
# for all elements of strs{
#     temp = {a->z:0}
#     for 
# }