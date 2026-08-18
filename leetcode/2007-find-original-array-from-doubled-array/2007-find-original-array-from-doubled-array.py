class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        count = Counter(changed)
        changed.sort()

        ans = []
        if len(changed)%2 != 0:
            return []
        for num in changed:
            if count[num] ==0 :continue

            if count[num*2] <=0: return []

            count[num] -= 1
            count[num*2] -= 1
            ans.append(num)
        
        return ans







        