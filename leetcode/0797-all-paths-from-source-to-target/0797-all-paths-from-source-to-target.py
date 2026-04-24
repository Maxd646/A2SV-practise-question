class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)-1
        ans = []
        queue = deque([[0]])
        while queue:
            path = queue.popleft()
            node = path[-1]
            if node ==n:
                ans.append(path)
                continue
            for child in graph[node]:
                queue.append(path + [child])
        return ans







       


        