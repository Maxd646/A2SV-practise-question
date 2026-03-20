class Solution:
    def longestPrefix(self, pattern: str) -> str:
        n = len(pattern)
        lps = [0] * n

        le = 0
        i = 1

        while i < n:
            if pattern[i] == pattern[le]:
                le += 1
                lps[i] = le
                i += 1
            else:
                if le != 0:
                
                    le = lps[le - 1]
                else:
                    lps[i] = 0
                    i += 1
        return pattern[:lps[-1]]
    
        