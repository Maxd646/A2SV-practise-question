class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:

        n = len(parent)
        seen = defaultdict(list)

        for i in range(n):
            seen[parent[i]].append(i)

        h = -1
        que = deque([-1])

        while que:
            h += 1
            node = [que.popleft() for _ in range(len(que))]

            for n in node:
                for val in seen[n]:
                    que.append(val)
        
        que = deque([-1])
        d = 0
        ans = 0
        
        while que:

            nodes = [que.popleft() for _ in range(len(que))]
            d += 1

            for node in nodes:

                for val in seen[node]:

                    ans +=  nums[val] *(h-d+1)

                    que.append(val)
        return ans
        
           
        
        
        
            

           
        
      

        