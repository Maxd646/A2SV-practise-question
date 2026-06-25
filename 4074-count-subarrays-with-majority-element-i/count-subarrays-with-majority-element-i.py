class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = 0
        for i in range(len(nums)):
            total = 0 
            a = 0
            for j in range(i, len(nums)):
                total +=1
                if nums[j] == target:
                    a+=1
                if a>(total-a):
                    ans+=1
        return ans


        