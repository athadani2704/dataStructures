class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        store = set()
        j = 10
        result = set()
        for i in range(len(s)-9):
            val = s[i:j]
            if val not in store:
                store.add(val)
            else:
                result.add(val)
            j += 1
        return result