class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n= len(costs)
        ans= []
        for a, b in costs:
            ans.append([b-a, a, b])
        res=0
        ans.sort()
        for i in range(n):
            if i<n//2:
                res+=ans[i][2]
            else:
                res+=ans[i][1]
        return res

        