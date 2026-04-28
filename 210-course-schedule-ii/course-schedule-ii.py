class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming = [0 for _ in range(numCourses)]
        
        for num, val in  prerequisites:
            graph[val].append(num)
            incoming[num] += 1
        # print(graph, incoming)
        queue = deque()
        ans = []
        for val in range(numCourses):
            if incoming[val] == 0:
                queue.append(val)
        # print(queue)
        while queue:
            course = queue.popleft()
            ans.append(course)

            for ne in graph[course]:
                incoming[ne] -= 1
                if incoming[ne] == 0:
                    queue.append(ne)
        # print(ans)
        if len(ans) == numCourses:
            return ans
        return []