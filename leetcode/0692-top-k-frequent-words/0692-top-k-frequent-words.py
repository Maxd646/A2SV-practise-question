class Solution:
    def topKFrequent(self, words: List[str], k: int) -> Lis(t[str]):
        arr = sorted(Counter(words).items(), key = lambda x:(-x[1], x[0]))[:k]
        res = []
        for word, _ in arr:
            res.append(word)
        return res
        

        