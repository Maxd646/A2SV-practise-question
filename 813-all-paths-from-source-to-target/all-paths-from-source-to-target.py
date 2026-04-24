class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)-1
        ans = []
        def dfs(node, path):
            if node == n:
                ans.append(path[:])
                return 
            for child in graph[node]:
                path.append(child)
                dfs(child, path)
                path.pop()
        dfs(0, [0])
        return ans
        
        return ans







       


        