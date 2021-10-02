class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if len(dungeon)==1 and len(dungeon[0])==1:
            return 1 if dungeon[0][0]>0 else 1+abs(dungeon[0][0])
        arr = dungeon
        r, c = len(arr), len(arr[0])
        arr[r-1][c-1] = abs(arr[r-1][c-1])+1 if arr[r-1][c-1]<0 else 1
        for i in range(r-2, -1, -1):
            arr[i][c-1] = max(1, arr[i+1][c-1]-arr[i][c-1])
        for i in range(c-2, -1, -1):
            arr[r-1][i] = max(1, arr[r-1][i+1]-arr[r-1][i])
        for i in range(r-2, -1, -1):
            for j in range(c-2, -1, -1):
                m = min(arr[i+1][j], arr[i][j+1])
                arr[i][j] = max(1, m-arr[i][j])
        return arr[0][0]
 
# - set r = len of dungeon and c = len of dungeion[0]
# - set bottom right cell value as abs(given value)+1 if given value<0 otherwise 1
# - loop through from r-1 to 1
#     - set dungeon[i][c] = max of 1 and dungeon[i+1][c]-dungeon[i][c]
# - loop through from c-1 to 1
#     - set dungeon[r][i] = max of 1 and dungeon[r][i+1]-dungeon[r][i]
# - loop through from i=r-1 to 1
#     - loop through from j=c-1 to 1
#         - set m = min of dungeon[i+1][j] and dungeon[i][j+1]
#         - set dungeon[i][j] = max of 1 and m-dungeon[i][j]
# - return dungeon[0][0]