class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        seen= Counter(s)
        if len(seen)<=k:
            return 0
        seen= sorted(seen.items(), key= lambda x: x[1], reverse=True)
        ans=0
        for num, val in seen[k:]:
            ans+=val
        return ans



        
        
        
            
        

        