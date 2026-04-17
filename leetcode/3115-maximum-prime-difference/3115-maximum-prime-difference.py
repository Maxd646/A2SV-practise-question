class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        prime = [True]*(max(nums)+1)
        prime[0], prime[1] = False, False
        p = 2
        while p*p<=max(nums)+1:
            if prime[p]:
                for i in range(p*p, max(nums)+1, p):
                    prime[i] =False
            p+=1
        ans =[]
        for i in range(len(nums)):
            if prime[nums[i]]:
                ans.append(i)
        return max(ans)- min(ans)
       


        