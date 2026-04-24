class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)
        for i in range(n):
            x, y, r = bombs[i]
            for j in range( n):
                xi, yi, _ = bombs[j]
                if i == j:
                    continue
                distance = math.sqrt((xi - x) ** 2 + (yi - y) ** 2)
                if r >= distance:
                    graph[i].append(j)
        lru_cache(None)
        def dfs(node, visited):
            visited.add(node)
            count = 1
            for child in graph[node]:
                if child not in visited:
                    count += dfs(child, visited)
            return count
        maxx = 0
        for i in range(n):
            visited = set()
            maxx = max(maxx, dfs(i, visited))
        return maxx
            



        
        


        
        




        