class Solution:
    def compress(self, chars: List[str]) -> int:

        stack = []
        ans = []

        for i in range(len(chars)):
            if not stack:
                stack.append(chars[i])
                continue
            
            if stack[-1] != chars[i]:
                ans.append(stack[-1])

                if len(stack) != 1:
                    ans.extend(list(str(len(stack))))

                stack.clear()
                stack.append(chars[i])
                
                continue

            stack.append(chars[i])
        
        ans.append(stack[-1])

        if len(stack) != 1:
            ans.extend(list(str(len(stack))))

        chars[:len(ans)] = ans

        return len(ans)
       
            
                
        