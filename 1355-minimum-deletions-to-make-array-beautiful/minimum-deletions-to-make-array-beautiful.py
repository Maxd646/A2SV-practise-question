class Solution:
    def minDeletion(self, nums: List[int]) -> int:

        stack  = []
        ans = 0
        for num in nums:
            
            if stack and stack[-1] == num and len(stack)%2 != 0:
                ans+=1
                continue
            stack.append(num)
        if len(stack)%2 != 0:
            return ans +1
        return ans
        