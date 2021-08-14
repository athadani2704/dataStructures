class Solution:
    def findSolution(self, i, rooms, visited, leadsTo):
        # print(i, leadsTo)
        if len(rooms[i])==0:
            return set()
        if i in leadsTo:
            return leadsTo[i]
        leadsTo[i] = set()
        for room in rooms[i]:
            if room in visited:
                continue
            visited.add(room)
            curSet = self.findSolution(room, rooms, visited, leadsTo)
            leadsTo[i].update(curSet)
            leadsTo[i].update(set([room]))
            visited.remove(room)
        return leadsTo[i]
        
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        leadsTo = {}
        return len(self.findSolution(0, rooms, visited, leadsTo))==len(rooms)-1
        
# currentRoom = 0
# visited = set(0)
# leadsTo = {key=number: value=set()}
# function(currentRoom, visited, leadsTo){
#     - check if current room is empty
#         if yes then return set()
#     - check if leadsTo contains currentRoom
#         if yes then return list of all rooms it can lead to
#         if no then 
#             add nextRoom to visited
#             initialize empty set and add elements returned from function(nextRoom, visited, leadsTo)
#             remove nextRoom from visited
# }


# [1,3],[3,0,1],[2],[0]

# 1 -> 3 -> 0
#   -> 0X
#   -> 1X