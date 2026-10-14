class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        n , m  = len(grid), len(grid[0])

        def dfs(i, j):


            if i>=n or i<0 or j >= m or j<0 or grid[i][j] == "0":
                return 

    

            grid[i][j] = "0"

            for x, y in [(1, 0), (0, 1), (-1, 0), (0,-1)]:

                a = x+i
                b = y + j

                dfs(a, b)

        ans = 0
           
        for i in range(n):
            for j in range(m):

                if grid[i][j] == "1":

                    ans += 1

                    dfs(i, j)
        return ans 






       

                
        