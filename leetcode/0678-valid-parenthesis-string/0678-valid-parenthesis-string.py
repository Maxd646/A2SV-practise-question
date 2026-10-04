class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        sstack = []

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)

            elif ch == "*":
                sstack.append(i)

            else:  
                if stack:
                    stack.pop()

                elif sstack:
                    sstack.pop()
                else:
                    return False

        
        while stack and sstack:

            if stack[-1] > sstack[-1]:
                return False

            stack.pop()
            sstack.pop()

        return not stack
