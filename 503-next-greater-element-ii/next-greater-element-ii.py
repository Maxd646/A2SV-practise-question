class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = [-1]*2*n
        nums=nums+nums
        for i in range(2*n-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i] :

                stack.pop()
            if stack:

                ans[i]=nums[stack[-1]]
                
            stack.append(i)
        return ans[:n]