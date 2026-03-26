class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans= []
        comb= []
        def backtrack(start, rem):
            if rem==0:
                ans.append(comb[:])
                return 
            if rem<0:
                return 
            for i in range(start,len(candidates)):
                comb.append(candidates[i])
                backtrack(i, rem-candidates[i])
                comb.pop()
        backtrack(0, target)
        return ans
        