class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        for i in range(left, right+1):
            if i<=9:
                ans.append(i)
                continue
            nu=str(i)
            found=False
            for ch in nu:
                if ch=="0":
                    found=True
                    break
                elif i%int(ch)!=0:
                    found=True
                    break
            if not found:
                ans.append(i)
        return ans
            
        
        