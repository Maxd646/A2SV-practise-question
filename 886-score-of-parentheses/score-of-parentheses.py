class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans=0
        temp=0
        for i in range(len(s)):
            if s[i]=="(":
                temp+=1
            else:
                temp-=1
                if s[i-1]=="(":
                    ans+=2**temp
        return ans
    




            

        