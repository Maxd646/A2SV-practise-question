# Maximum Number of Coins You Can Get
# Platform: LeetCode
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        print(piles)
        Max=0
        count=0
        for i in range(len(piles)):
            if i%2==1 and count<len(piles)//3:
                count+=1
                Max+=piles[i]
        return Max
