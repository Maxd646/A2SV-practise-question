class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m= len(grid), len(grid[0])
        ans = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans.append(grid[i][j])
        k = k%(len(ans))
        ans = ans[-k:] +ans[:-k]
        num = []
        res= []
        for i in range(len(ans)):
            if (i+1)%m != 0:
                num.append(ans[i])
            else:
                num.append(ans[i])
                res.append(num)
                num = []
        return res
        
        


        
        
        

        