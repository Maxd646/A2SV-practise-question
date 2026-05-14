class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        num = math.prod(nums)
        # print(num)
        ans = set()
        i = 2
        while num>1:
            while num%i==0:
                ans.add(i)
                num//=i
            i+=1
        # print(ans)
        return len(list(ans))
                
            
        