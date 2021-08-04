class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        cache = set()
        self.findSolution(candidates, 0, 0, target, result, [], cache)
        return result
    
    def findSolution(self, arr, i, cur_sum, target, result, cur_path, cache):
        if cur_sum==target:
            if "_".join(sorted(list(map(str, cur_path)))) not in cache:
                result.append(cur_path)
                cache.add("_".join(sorted(list(map(str, cur_path)))))
            return
        if cur_sum>target or i==len(arr):
            return
        self.findSolution(arr, i, cur_sum+arr[i], target, result, cur_path+[arr[i]], cache)
        self.findSolution(arr, i+1, cur_sum+arr[i], target, result, cur_path+[arr[i]], cache)
        self.findSolution(arr, i+1, cur_sum, target, result, cur_path, cache)