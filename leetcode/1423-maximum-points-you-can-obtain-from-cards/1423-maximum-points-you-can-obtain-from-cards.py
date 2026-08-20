class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        left, right = 0, len(cardPoints)-k
        total = sum(cardPoints[right:])

        ans = total

        while right <len(cardPoints):

            total += cardPoints[left] - cardPoints[right]
            ans = max(ans, total)
            left +=1
            right += 1

        return ans


        


        