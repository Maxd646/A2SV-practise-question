class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans= []
        def backtrack(start, comb):
            if sum(comb)==target:
                ans.append(comb[:])
            if sum(comb)>target:
                return 
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                comb.append(candidates[i])
                backtrack(i+1, comb)
                comb.pop()
        backtrack(0, [])
        return list(set([tuple(sorted(seen)) for seen in ans]))
        
        