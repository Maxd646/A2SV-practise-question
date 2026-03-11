class Solution:
    def bitwiseComplement(self, n: int) -> int:
        num=bin(n)[2:]
        ans= []
        for i in range(len(num)):
            if num[i]=="1":
                ans.append("0")
            else:
                ans.append("1")
        return int("".join(ans), 2)
        
        

        