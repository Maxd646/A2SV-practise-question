class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod = 12345
        n, m = len(grid), len(grid[0])

        ans = [[1]*m for _ in range(n)]

        prex = 1
        for i in range(n):
            for j in range(m):
                ans[i][j] = prex
                prex = (grid[i][j]*prex)%mod
        
        sefix = 1
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                ans[i][j] = (sefix*ans[i][j])%mod
                sefix = (grid[i][j]*sefix)%mod
        return ans



     
        