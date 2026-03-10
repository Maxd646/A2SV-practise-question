class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != "]":
                stack.append(ch)

            else:
                temp = ""

                while stack and stack[-1] != "[":
                    temp = stack.pop() + temp

                stack.pop()  

                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                repeat = int(num) if num else 1
                expanded = temp * repeat

                for c in expanded:
                    stack.append(c)

        return "".join(stack)

                




        