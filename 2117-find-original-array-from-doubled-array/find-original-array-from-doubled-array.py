class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        count = Counter(changed)
        changed.sort()
        ans = []
        if len(changed)%2!= 0 or changed.count(0)%2!=0:
            return []
        for num in changed:
            if count[num]>0 and count[num*2]>0:
                ans.append(num)
                count[num*2] -= 1
                count[num]  -= 1
        if len(ans) == len(changed)/2:
            return ans
        return []






        