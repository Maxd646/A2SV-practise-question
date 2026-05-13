class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        size = [1]*len(edges)
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px =  find(x)
            py = find(y)
            if px != py:
                if size[px]>size[py]:
                    parent[py] = parent[px]
                    size[px] += size[py]
                else:
                    parent[px] = parent[py]
                    size[py] += size[px]

        for u, v  in edges:
            if find(v-1) == find(u-1):
                return [u, v]
            union(u-1, v-1)

             



        