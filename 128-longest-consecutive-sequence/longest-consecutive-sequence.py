class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen  = Counter()
        for num in nums:
            seen[num] = False
        ans = 0
        for num in nums:
            maxx = 1
            seen[num] = True
            nex = num +1
            while nex in seen and  not seen[nex]:
                maxx+=1
                seen[nex] = True
                nex+=1
            back = num-1
            while back in seen and not seen[back]:
                maxx+=1
                seen[back] = True
                back-=1
            ans = max(maxx, ans)
        return ans
                    


        