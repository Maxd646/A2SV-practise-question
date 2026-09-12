class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:

        ans = 1
        n = len(prizePositions)
        com = [0]*(n+1)

        count = 0
        left = 0

        for i in range(n):

            while prizePositions[i] - prizePositions[left] > k:
                left += 1

            count = i - left + 1

            ans = max(ans, count + com[left])

            com[i+1] = max(count, com[i])
            
        
        return ans
        
        