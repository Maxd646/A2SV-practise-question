class Solution:
    def minOperations(self, nums: list[int]) -> int:
        maxx = 2*10**5
        prime = [True]*(maxx+1)
        prime[0], prime[1] = False, False
        p = 2
        while p*p<=maxx:
            if prime[p]:
                for i in range(p*p, maxx+1, p):
                    prime[i] = False
            p+=1
        ans =0

        for i in range(len(nums)):
            if i % 2 == 0:
                if prime[nums[i]]:
                    continue
                j = 1
                while True:
                    x = nums[i] + j
                    if prime[x]:
                        ans += j
                        break
                    j += 1
            else:
                if prime[nums[i]]:
                    j = 1
                    while True:
                        x = nums[i] + j
                        if not prime[x]:
                            ans += j
                            break
                        j += 1     
        return ans
    