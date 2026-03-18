class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q=deque()
        for i in range(1, n+1):
            q.append(i)
        while len(q)>1:
            for j in range(k-1):
                m=q.popleft()
                q.append(m)
            q.popleft()
        return q[0]


        