class Solution:
    def topKFrequent(self, words: List[str], k: int) -> Lis(t[str]):
        arr = Counter(words)
        bucket =[[] for _ in range(len(words)+1)]
        for val, freq in arr.items():
            bucket[freq].append(val)
        res = []
        for freq in range(len(bucket)-1, 0, -1):
            if bucket[freq]:
                for word in sorted(bucket[freq]):
                    res.append(word)
                    if len(res)==k:
                        return res
        
        

        