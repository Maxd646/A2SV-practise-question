class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:


        suff = [nums[-1]]
        pre = [nums[0]]
        Max = nums[0]

        for num in nums[1:]:

            if num>Max:

                pre.append(num)
                Max = num
                continue

            pre.append(Max)
            
        Min = nums[-1]

        for num in nums[:-1][::-1]:

            if num < Min:

                suff.append(num)
                Min = num
                continue
            
            suff.append(Min)

        suff = suff[::-1]
        
        for i in range(len(pre)):

            if abs(pre[i] - suff[i]) <= k:

                return i
                
        return -1



        

        