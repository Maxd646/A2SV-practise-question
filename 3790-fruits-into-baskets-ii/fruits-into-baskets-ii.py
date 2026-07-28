class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        ans = 0
        Found = False
        for i in range(len(fruits)):
            Found = False
            for j in range(len(baskets)):
                if fruits[i]<=baskets[j]:
                    baskets[j] = 0
                    Found = True
                    break
            if not Found:
                ans+=1
        return ans
        