class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for word in  queries:
            for wor in dictionary:
                n = sum(1 for i in range(len(word)) if word[i]!=wor[i])
                if n<=2:
                    break
            if n<=2:
                ans.append(word)
        return ans
                


        