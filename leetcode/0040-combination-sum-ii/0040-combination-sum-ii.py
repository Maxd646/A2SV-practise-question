class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        ans = []
        candidates.sort()
        def dfs(index, path, summ):

            if summ == target:
                ans.append(path[:])
                return 
        
            if summ > target or index >= len(candidates):
                return 
            
            dfs(index +1, path + [candidates[index]], summ + candidates[index])
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1

            dfs (index +1, path, summ)
        dfs(0, [], 0)

        return list(set(tuple(sorted(num)) for num in ans))
        