class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        ref_set = set(s)
        options = []
        for word in words:
            flag = False
            if len(word)>len(s) or len(ref_set)!=len(set(word)):
                continue
            for val in set(word):
                if val not in ref_set:
                    flag = True
                    break
            if not flag:
                options.append(word)
        final_result = 0
        
        for word in options:
            i, j = 0, 0
            result = True
            while i<len(s):
                if j>=len(word) or s[i]!=word[j]:
                    result = False
                    break
                c = 1
                k = i+1
                while k<len(s) and s[k]==s[i]:
                    c += 1
                    k += 1
                k1 = j+1
                c1 = 1
                while k1<len(word) and word[k1]==word[j]:
                    c1 += 1
                    k1 += 1
                if c<c1 or (c>c1 and c<3):
                    result = False
                    break
                i = k
                j = k1
            final_result += result
        return final_result
            