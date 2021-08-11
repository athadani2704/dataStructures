class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        track = {}
        vals = set()
        for interval in intervals:
            track[interval[0]] = track.get(interval[0], 0)+1
            track[interval[1]] = track.get(interval[1], 0)-1
            vals.add(interval[0])
            vals.add(interval[1])
        result = counts = 0
        for val in sorted(list(vals)):
            counts += track[val]
            if counts>result:
                result = counts
        return result