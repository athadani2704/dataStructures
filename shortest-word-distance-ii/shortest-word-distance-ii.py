class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.arr = wordsDict

    def shortest(self, word1: str, word2: str) -> int:
        dist = len(self.arr)
        aloc, bloc = -1, -1
        for i, word in enumerate(self.arr):
            if word==word1:
                if bloc>-1 and i-bloc<dist:
                    dist = i-bloc
                aloc = i
            elif word==word2:
                if aloc>-1 and i-aloc<dist:
                    dist = i-aloc
                bloc = i
        return dist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)