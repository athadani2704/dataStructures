class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pos1 = pos2 = -1
        result = len(wordsDict)
        for i, word in enumerate(wordsDict):
            if word==word1:
                if pos2>=0 and i-pos2<result:
                    result = i-pos2
                pos1 = i
            elif word==word2:
                if pos1>=0 and i-pos1<result:
                    result = i-pos1
                pos2 = i
        return result