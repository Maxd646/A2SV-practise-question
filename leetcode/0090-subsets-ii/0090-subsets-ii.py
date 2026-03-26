class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n= len(nums)
        ans = []
        def backtrack(st, poss):
            ans.append(poss[:])
            for j in range(st, n):
                if j>st and nums[j]==nums[j-1]:
                    continue
                poss.append(nums[j])
                backtrack(j + 1, poss)
                poss.pop()
        
        backtrack(0, [])
        return ans
    
 

        