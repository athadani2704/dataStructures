class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        if len(s)==1:
            return 1
        i = j = 0
        result = 0
        freq = {}
        store = set()
        while j<len(s):
            if s[j] in store:
                freq[s[j]] = freq.get(s[j], 0)+1
            elif len(store)==2:
                while len(store)==2:
                    i += 1
                    freq[s[i-1]] -= 1
                    if freq[s[i-1]]==0:
                        store.remove(s[i-1])
                store.add(s[j])
                freq[s[j]] = freq.get(s[j], 0)+1
            else:
                store.add(s[j])
                freq[s[j]] = freq.get(s[j], 0)+1
            j += 1
            if j-i>result:
                result = j-i
        return result

                    
