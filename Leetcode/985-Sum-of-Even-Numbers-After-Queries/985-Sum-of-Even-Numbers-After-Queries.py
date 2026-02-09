# Sum of Even Numbers After Queries
# Platform: LeetCode

class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        result= []
        summ=sum(num for num in nums if num%2==0)
        for val, i in queries:
            if nums[i]%2==0:
                summ-=nums[i]
            nums[i]=nums[i]+val
            if nums[i]%2==0:
                summ+=nums[i]
            result.append(summ)
        return result
           
