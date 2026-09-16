class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        seen = set(wordDict)
        n = len(s)
        res = [False] *(n+1)

        res[0] = True

        for i in range(n+1):

            for word in seen:

                if res[i] and (i+ len(word)) <= n and s[i:i+len(word)] in seen:
                    res[i+len(word)] = True
                    
        return res[n]

        