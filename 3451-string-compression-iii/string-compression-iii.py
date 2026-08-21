class Solution:
    def compressedString(self, chars: str) -> str:

        stack = []
        ans = []

        for i in range(len(chars)):
            if not stack:
                stack.append(chars[i])
                continue
            
            if stack[-1] != chars[i] or len(stack) ==9:
                ans.append(str(len(stack)))
                ans.append(stack[-1])
                stack.clear()
                stack.append(chars[i])
                
                continue

            stack.append(chars[i])

        ans.append(str(len(stack)))
        ans.append(stack[-1])

        return "".join(ans)
       
            
                
        
        