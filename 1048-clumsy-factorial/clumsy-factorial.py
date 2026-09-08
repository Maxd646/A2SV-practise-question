class Solution:
    def clumsy(self, n: int) -> int:
        
        stack = [n]
        n -= 1
        op = 0

        while n > 0:
            
            if op == 0:
                stack[-1] *= n

            elif op == 1:
                stack[-1] = int(stack[-1] / n)

            elif op == 2:
                stack.append(n)

            else:
                stack.append(-n)

            n -= 1
            op = (op + 1) % 4

        return sum(stack)