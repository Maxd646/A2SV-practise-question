class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1]*(nums[i-1]))

        sefix = [1]*len(nums)
        pro = 1
        for i in range(len(nums)-1, 0, -1):
            sefix[i-1] = sefix[i]*(nums[i])
        
        ans = [1]*len(nums)

        for i in range(len(nums)):
            ans[i] = sefix[i]*prefix[i]
       
        return ans
        

        