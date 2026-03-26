class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans= []
        def backtrack(start, comb):
            if sum(comb)==target:
                ans.append(comb[:])
            if sum(comb)>target:
                return 
            for i in range(len(candidates)):
                comb.append(candidates[i])
                backtrack(i, comb)
                comb.pop()
        backtrack(0, [])
        return list(set([tuple(sorted(seen)) for seen in ans]))
        