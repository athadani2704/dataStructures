class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        result = 0
        nbox = 0
        for n, units in boxTypes:
            if n+nbox<=truckSize:
                result += n*units
                nbox += n
            else:
                result += (truckSize-nbox)*units
                break
        return result