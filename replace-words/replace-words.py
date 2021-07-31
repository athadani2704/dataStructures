class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = sorted(dictionary, key=lambda x: len(x))
        freq = {}
        maxlen = 0
        for word in dictionary:
            freq[len(word)] = freq.get(len(word), [])+[word]
            if len(word)>maxlen:
                maxlen = len(word)
        result = []
        for word in sentence.split():
            cur = ''
            flag = False
            for i, alpha in enumerate(word):
                cur += alpha
                if i+1 in freq and cur in freq[i+1]:
                    result.append(cur)
                    flag = True
                    break
                elif i+1>maxlen:
                    break
            if not flag:
                result.append(word)
        return ' '.join(result)