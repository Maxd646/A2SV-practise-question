class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph =  [[] for _ in range(n)]
        for i in range(n):
            x, y, r = bombs[i]
            for j in range(n):
                if i== j:
                    continue
                xi, yi, _ = bombs[j]
                distance = ((abs(x-xi)**2+abs(y-yi)**2))**0.5
                if r>=distance:
                    graph[i].append(j)
        lru_cache(None)
        def dfs(node, visited):
            nonlocal count
            visited.add(node)
            count+=1
            for child in graph[node]:
                if child not in visited:
                    dfs(child, visited)
        maxx = 0
        for i in range(n):
            count = 0
            dfs(i, set())
            maxx = max(maxx, count)
        return maxx
            



        
        


        
        




        