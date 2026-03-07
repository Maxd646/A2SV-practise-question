class Solution:
    def minFlips(self, s: str) -> int:
        minn=float("inf")
        d1=0
        d2=0
        n=len(s)
        s=list(map(int, s+s))
        aa=[i%2 for i in range(n*2)]
        bb=[(i+1)%2 for i in range(n*2)]
        l=0
        for i in range(n*2):
            if s[i]!=aa[i]:
                d1+=1
            if s[i]!=bb[i]:
                d2+=1
            while i-l+1>n:
                if s[l]!=aa[l]:
                    d1-=1
                if s[l]!=bb[l]:
                    d2-=1
                l+=1
            if i-l+1==n:
                minn=min(minn, d1, d2)
        return minn


        
        
        