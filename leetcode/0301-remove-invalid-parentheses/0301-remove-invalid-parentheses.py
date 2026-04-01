class Solution:
    def isValidString(self, temp):
        cnt = 0
        for i in range(len(temp)):
            if temp[i] == '(':
                cnt += 1
            elif temp[i] == ')':
                cnt -= 1
            if cnt < 0:
                return False
    
        return cnt == 0 
    def removeInvalidParentheses(self, s: str) -> List[str]:
        visit = {}
        q = deque()
        res = []
        level = False
        q.append(s)
        visit[s] = 1
        while q:
            temp = q.popleft()
            if self.isValidString(temp):
                res.append(temp)
                level = True
            if level:continue

            for i in range(len(temp)):

                if temp[i] != '(' and temp[i] != ')':
                    continue
                cur = temp[:i] + temp[i + 1:]
                if cur not in visit:
                    q.append(cur)
                    visit[cur] = 1
        return res

   
  
        