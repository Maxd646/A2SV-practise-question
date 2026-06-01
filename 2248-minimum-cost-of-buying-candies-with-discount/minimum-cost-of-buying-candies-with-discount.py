class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        ans = 0
        if len(cost)<=3:
            return sum(cost[:2])
        for i in range(0, len(cost), 3):
            ans+= cost[i]
            if i+1<len(cost):
                ans+= cost[i+1]
        return ans



            
        
        
        