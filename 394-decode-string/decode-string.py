class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        temp = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num=num*10+int(ch)
            elif ch=="[":
                stack.append((temp, num))
                temp=""
                num=0
            elif ch=="]":
                st, n= stack.pop()
                temp=st+temp*n
            else:
                temp+=ch
        return temp
                