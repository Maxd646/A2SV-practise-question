class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        if not relations:
            return max(time)
        graph = defaultdict(list)
        incoming = [0]*(n+1)
        ans = [0] * (n + 1)

        for pre, nex in relations:
            graph[pre].append(nex)
            incoming[nex] += 1
     
        
        q = deque()
      
        for i in range(1, n+1):
            if incoming[i]==0:
                q.append(i)
        while q:
            for _  in range(len(q)):
                node = q.popleft()
                ans[node] += time[node - 1]
                for ch in graph[node]:
                    ans[ch] = max(ans[ch], ans[node]) 
                    incoming[ch] -= 1
                    if incoming[ch] == 0:
                        q.append(ch)
       
        return max(ans)
        