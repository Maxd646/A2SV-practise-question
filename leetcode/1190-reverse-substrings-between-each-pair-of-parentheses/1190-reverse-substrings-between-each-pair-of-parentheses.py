class Solution:
    def reverseParentheses(self, s: str) -> str:

        stack = []
        ans = ""
        
        n = len(s)
        yes = True

        for i in range(n):

            if s[i] == ")":
                temp = ""
                while stack[-1] != "(":

                    temp += stack.pop()
               
                stack.pop()
                stack.extend(temp)
                continue 

            stack.append(s[i])

        
        return "".join(stack)
            

            

        