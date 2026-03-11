class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n= len(nums)
        qI = deque()
        qD = deque()
        ans=1
        l=0
        for i in range(n):
            while qI and qI[-1]>nums[i]:
                qI.pop()
                
            while qD and qD[-1]<nums[i]:
                qD.pop()

            qI.append(nums[i])
            qD.append(nums[i])

            while qI and qD and qD[0]-qI[0]>limit:
                if nums[l]== qD[0]:
                    qD.popleft()
                if nums[l]== qI[0]:
                    qI.popleft()
                l+=1

            ans=max(ans, i-l+1)
        return ans
            
            

            


            
        
       


        