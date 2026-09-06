class Solution:
    def maxProduct(self, words: List[str]) -> int:

        sets = [set(word) for word in words]
        ans = 0

        for i in range(len(words)):

            for j in range(i + 1, len(words)):

                if sets[i].isdisjoint(sets[j]):
                    
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans

        