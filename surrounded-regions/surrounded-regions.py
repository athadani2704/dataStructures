class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited, notPossible = set(), set()
        r, c = len(board), len(board[0])
        if r==1 or c==1:
            return
        arr = board
        avoid = [[[0,False] for j in range(c)] for i in range(r)]
        for i in [0, r-1]:
            for j in range(c):
                if arr[i][j]=="O":
                    self.update(arr, r, c, i, j, avoid)
        for j in [0, c-1]:
            for i in range(r):
                if arr[i][j]=="O":
                    self.update(arr, r, c, i, j, avoid)
        for i in range(r):
            for j in range(c):
                if arr[i][j]=="O" and not avoid[i][j][1]:
                    arr[i][j] = "X"
        
    def update(self, arr, r, c, i, j, avoid):
        if i<0 or i==r or j<0 or j==c:
            return
        if avoid[i][j][0]:
            return
        avoid[i][j][0] = 1
        if arr[i][j]=="O":
            avoid[i][j][1] = True
            self.update(arr, r, c, i-1, j, avoid)
            self.update(arr, r, c, i, j-1, avoid)
            self.update(arr, r, c, i+1, j, avoid)
            self.update(arr, r, c, i, j+1, avoid)
        