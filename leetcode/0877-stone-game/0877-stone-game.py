class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        @lru_cache(None)
        def df(i, j):
            if i == j:
                return piles[i]

            return max(
                piles[i] - df(i + 1, j),
                piles[j] - df(i, j - 1)
            )

        return df(0, n - 1) >= 0
        