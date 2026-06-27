class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ans = 1
        count = Counter(nums)
        if 1 in count:
            ans = max(ans, count[1] if count[1] % 2 else count[1] - 1)

        for x in count:
            res = 0
            if x == 1: continue
            else:
                curr = x
                while count[curr]>=2:
                    curr = curr*curr
                    res+=2
                if count[curr]==1:
                    res+=1
                else:
                    res-=1
            ans = max(res, ans)
        return ans


        