class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for ch in nums1:
            i=0
            found=False
            yes=False
            while i<len(nums2):
                if ch==nums2[i]:
                    found=True
                elif found and nums2[i]>ch:
                    result.append(nums2[i])
                    yes=True
                    break
                i+=1
            if not yes:
                result.append(-1)
        return result
            
                    
                




        