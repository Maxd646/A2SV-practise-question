class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:

        if k >= len(arr):
            return max(arr)

        queu = deque(arr)
        seen = Counter()

        while True:

            if queu[0] > queu[1]:
                winner = queu.popleft()
                loser = queu.popleft()

            else:
                loser = queu.popleft()
                winner = queu.popleft()

            seen[winner] += 1

            if seen[winner] >= k:
                return winner

            queu.appendleft(winner)
            queu.append(loser)