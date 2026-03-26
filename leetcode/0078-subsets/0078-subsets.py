class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(st, poss, l):
            if len(poss) == l:
                ans.append(poss[:])
                return
            for j in range(st, n):
                poss.append(nums[j])
                backtrack(j + 1, poss, l)
                poss.pop()
        ans = []
        n= len(nums)
        for i in range(n+ 1):
            backtrack(0, [], i)
        return ans
    
 
        
        
    
        