class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustRec = {}
        if trust==[]:
            return 1 if n==1 else -1
        judgeOpt = set([k for k in range(1, n+1)])
        for give, rec in trust:
            trustRec[rec] = trustRec.get(rec, [])+[give]
            if give in judgeOpt:
                judgeOpt.remove(give)
        for k, v in trustRec.items():
            if k in judgeOpt and len(v)==n-1:
                return k
        return -1