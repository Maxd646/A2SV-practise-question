class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node, graph):
            temp = True
            for neighbour in graph[node]:
                if grid[neighbour] == -1:
                    if grid[node] == 0:
                        grid[neighbour] = 1
                    else:
                        grid[neighbour] = 0
                    temp = temp and dfs(neighbour, graph)
                elif grid[node] == grid[neighbour]:
                    return False
            return temp

        n = len(graph)
        grid  = [-1 for _ in range(n)]
        temp = True
        for i in range(n):
            if grid[i]==-1:
                grid[i]=0
                temp = temp and dfs(i, graph)
        return temp




        
        