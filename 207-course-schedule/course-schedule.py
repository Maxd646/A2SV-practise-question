class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        incoming = [0 for _ in range(numCourses)]
        for pre, val in prerequisites:
            graph[val].append(pre)
            incoming[pre]+=1

        queue = deque()
        for val in range(numCourses):
            if incoming[val]==0:
                queue.append(val)
        ans = []
        while queue:
            course = queue.popleft()
            ans.append(course)
            for neg in graph[course]:
                incoming[neg]-=1
                if incoming[neg] ==0:
                    queue.append(neg)
        return len(ans) == numCourses

        
            
        
        