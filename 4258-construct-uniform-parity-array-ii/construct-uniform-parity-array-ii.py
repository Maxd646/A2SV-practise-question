class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd = 0
        seen = []
        for num in nums1:
            if num%2!=0:
                odd+=1
                seen.append(num)
        if odd == len(nums1) or odd == 0:
            return True
        seen.sort()
        # print(seen)
        for num in nums1:
            if num%2==0:
                x = bisect.bisect_left(seen, num)
                if x==0:
                    return False
        return True
            
            
        
        
        