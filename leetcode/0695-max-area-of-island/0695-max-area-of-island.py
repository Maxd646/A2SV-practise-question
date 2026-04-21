class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        count = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0])) and (grid[row][col]!=0)
        def dfs(row, col):
            nonlocal count
            if not inbound(row, col):
                return
            grid[row][col]  = 0
            for i, j in directions:
                nr, nc= i+row, j+col
                if inbound(nr, nc):
                    count+=1
                    dfs(nr, nc)
                
        maxx = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] ==1:
                    count = 1
                    dfs(i, j)
                    maxx = max(count, maxx)
                   
        return maxx
            
        