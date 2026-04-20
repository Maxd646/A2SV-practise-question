from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for v, u in edges:
            graph[v].append(u)
            graph[u].append(v)

        visited = set()
        stack = [source]
        print(graph)
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                stack.extend(graph[node])
        return False