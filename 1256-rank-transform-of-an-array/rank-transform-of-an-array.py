class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        Rank = {}
        Sorted = sorted(arr)
        rank = 1
        for i in range(len(Sorted)):
            if i > 0 and Sorted[i] > Sorted[i - 1]:
                rank += 1
            Rank[Sorted[i]] = rank
        for i in range(len(arr)):
            arr[i] = Rank[arr[i]]
        return arr