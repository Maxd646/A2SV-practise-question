class Solution:
    def minArraySum(self, nums: list[int]) -> int:

        m = max(nums)

        arr = [False]*(m+1)

        for num in nums:

            arr[num] = True

        ans  = [0]*(m+1)

        for d in range(1, m+1):

            if arr[d]:

                for j in range(d, m+1, d):

                    if arr[j]:

                        arr[j] = False
                        ans[j] = d

        return sum(ans[x] for x in nums)

        
        