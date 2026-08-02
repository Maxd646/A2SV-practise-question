class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
       
        seen = Counter()
        for i in range(len(senders)):
            seen[senders[i]] += len(messages[i].split())
        ans = ""
        maxx = 0
        for nu, val in seen.items():
            if val> maxx:
                ans = nu
                maxx = val
            elif val == maxx:
                ans = max(ans, nu)
        return ans

            

        