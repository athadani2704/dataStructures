class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        for i in range(len(s)):
            if (t[i] in tdict and tdict[t[i]]!=s[i]) or (s[i] in sdict and sdict[s[i]]!=t[i]):
                return False
            else:
                if t[i] not in tdict:
                    tdict[t[i]] = s[i]
                if s[i] not in sdict:
                    sdict[s[i]] = t[i]
        return True
    
    
    
    