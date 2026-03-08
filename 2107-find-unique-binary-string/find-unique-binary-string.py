class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans= list(map(lambda x:(int(x, 2)), nums))
        seen= set(ans)
        n=int(("1"*len(nums)), 2)
        print(n)
       
        for i in range(n+1):
            if i not in seen:
                return bin(i)[2:].zfill(len(nums))
                
        