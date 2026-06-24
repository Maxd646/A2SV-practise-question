class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        
        rank = {ch: [0] * n for ch in votes[0]}
        
        for vote in votes:
            for i, ch in enumerate(vote):
                rank[ch][i] += 1
        return "".join(sorted(rank.keys(), key=lambda x: ([-rank[x][i] for i in range(n)], x)))
       