class Solution:
    def evaluate(self, s: str, ke: List[List[str]]) -> str:
        count = defaultdict(str)
        for key, val in ke:
            count[key] = val
        seen = Counter()
        flag = False
        ans =""
        key =""
        for i in range(len(s)):
            if s[i]=="(":
                flag = True
            elif s[i]==")":
                flag = False
                if count[key]:
                    ans+=count[key]
                else:
                    ans+="?"
                key =""
            elif flag:
                key+=s[i]
            else:
                ans+=s[i]
        return ans
        
        
        
        
       
        
        
            
        

            
            
