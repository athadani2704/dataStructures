class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        firstmax, secondmax, thirdmax = target
        current = [0, 0, 0]
        for current_value in triplets:
            if current_value[0]>firstmax or current_value[1]>secondmax or current_value[2]>thirdmax:
                continue
            if current_value[0]==firstmax or current_value[1]==secondmax or current_value[2]==thirdmax:
                current = [max(current[0],current_value[0]), max(current[1], current_value[1]), max(current[2], current_value[2])]
            if current==target:
                return True
        return False
                