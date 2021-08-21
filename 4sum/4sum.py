class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        if len(nums)<4:
            return result
        freq = {}
        for val in nums:
            freq[val] = freq.get(val, 0)+1
        two_sums = {}
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] not in two_sums:
                    smaller, larger = min(nums[i], nums[j]), max(nums[i], nums[j])
                    two_sums[nums[i]+nums[j]] = set([str(nums[i])+"_"+str(nums[j])])
                else:
                    two_sums[nums[i]+nums[j]].add(str(nums[i])+"_"+str(nums[j]))
        visited = set()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                self.findSolution(nums, nums[i], nums[j], result, two_sums, visited, freq, target-(nums[i]+nums[j]))
        return result
    
    def findSolution(self, nums, a, b, result, two_sums, visited, freq, comp):
        if comp not in two_sums:
            return
        for vals in two_sums[comp]:
            pair = list(map(int, vals.split("_")))
            combination = sorted([a, b]+pair)
            key = "_".join(list(map(str, combination)))
            if key in visited:
                continue
            invalid = False
            if a in pair or b in pair:
                for x in set(combination):
                    if combination.count(x)>freq[x]:
                        invalid = True
                        break
            if not invalid:
                visited.add(key)
                result.append(combination)