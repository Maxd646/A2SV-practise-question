class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = None
        stack = [False]*10
        path = []
        def backtrack():
            nonlocal ans
            if ans is not None:
                return 
            if len(path ) == len(pattern)+1:
                ans = "".join(path)
                return
            for i in range(1, 10):
                if stack[i]:
                    continue
                if path:
                    prev = int(path[-1])
                    if pattern[len(path) -1] == "I" and prev > i:
                        continue
                    if  pattern[len(path) -1]  == "D" and prev < i:
                        continue
                stack[i]  =  True
                path.append(str(i))
                backtrack()
                path.pop()
                stack[i] = False

        backtrack()
        return ans
            
       
        
        