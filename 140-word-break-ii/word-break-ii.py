class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:

        seen = set(wordDict)
        n = len(s)

        res = [[] for _ in range(n + 1)]
        res[0] = [""]

        for i in range(n):

            if not res[i]:
                continue

            for word in seen:

                end = i + len(word)

                if end <= n and s[i:end] == word:

                    for sentence in res[i]:

                        if sentence:

                            res[end].append(sentence + " " + word)

                        else:
                            res[end].append(word)
       
        return res[n]
