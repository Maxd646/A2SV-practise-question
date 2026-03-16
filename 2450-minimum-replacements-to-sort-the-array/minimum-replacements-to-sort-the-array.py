class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        nums=nums[::-1]
        a=nums[0]
        opt=0
        for i in range(len(nums)):
            if a<nums[i]:
                c = math.ceil(nums[i]/a )
                opt+=c-1
                a=nums[i]//c
            else:
                a=nums[i]
        return opt

        