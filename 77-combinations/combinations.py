class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans= []
        def backtracking(aa, comb):
            if len(comb)==k:
                ans.append(comb[:])
                return 

            for i in range(aa, n+1):
                comb.append(i)
                backtracking(i+1, comb)
                comb.pop()

        backtracking(1, [])
        return ans 
                


           
            
        
        