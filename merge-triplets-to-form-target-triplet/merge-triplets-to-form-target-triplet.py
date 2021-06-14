class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        firstmax, secondmax, thirdmax = target
        current = [0, 0, 0]
        for current_value in triplets:
            # if any of the triplet's current element is greater than required max value then ignore
            if current_value[0]>firstmax or current_value[1]>secondmax or current_value[2]>thirdmax:
                continue
            # if any of the triplet's current element is equal to required max value then consider max of this and last max value
            if current_value[0]==firstmax or current_value[1]==secondmax or current_value[2]==thirdmax:
                current = [max(current[0],current_value[0]), max(current[1], current_value[1]), max(current[2], current_value[2])]
            # check if target reached
            if current==target:
                return True
        return False
                
