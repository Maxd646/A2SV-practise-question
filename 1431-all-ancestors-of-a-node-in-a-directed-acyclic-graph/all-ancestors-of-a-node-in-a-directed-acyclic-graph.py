class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        incoming =[0 for _ in range(n)]
        for fro, to in edges:
            graph[fro].append(to)
            incoming[to]+=1
        
        queue= deque()
        for i in range(n):
            if incoming[i]==0:
                queue.append(i)
        ans = []
        while queue:
            fro = queue.popleft()
            ans.append(fro)
            for neg in graph[fro]:
                incoming[neg] -= 1
                if incoming[neg] ==0:
                    queue.append(neg)

        res = [[] for _ in range(n)]
        ancesstors = [set() for _ in range(n)]
        for node in ans:
            for neg in graph[node]:
                ancesstors[neg].add(node)
                ancesstors[neg].update(ancesstors[node])
        print(ancesstors)
        for i in range(n):
            res[i]= sorted(list(ancesstors[i]))

        return res
        
            

        
        
       
    


        

        
        