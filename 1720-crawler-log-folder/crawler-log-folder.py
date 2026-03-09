class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack =[]
        for chars in logs:
            if chars=="../":
                if stack:
                    stack.pop()
            elif chars=="./":
                continue
            else:
                stack.append(chars)
        return len(stack)
        