class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        result = 0
        dirs = [(-1,0), (0,-1), (1,0), (0,1)]
        for i in range(r):
            for j in range(c):
                if grid[i][j]=="1":
                    grid[i][j] = "2"
                    self.countIsland(grid, i, j, r, c, dirs)
                    result += 1
        return result
        
    def countIsland(self, arr, i, j, r, c, dirs):
        for y, x in dirs:
            if i+y>=0 and i+y<r and j+x>=0 and j+x<c and arr[i+y][j+x]=="1":
                arr[i+y][j+x] = "2"
                self.countIsland(arr, i+y, j+x, r, c, dirs)