class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        prefix = [0]+ list(accumulate(cardPoints))

        suffix = [0] + list(accumulate(cardPoints[::-1]))
        
        if len(cardPoints)<=k:
            return prefix[-1]
        maxx = 0
        n= len(cardPoints)-1
      

        for i in range(k+1):
            maxx = max(maxx, prefix[i]+suffix[k-i])
            

        return maxx




        