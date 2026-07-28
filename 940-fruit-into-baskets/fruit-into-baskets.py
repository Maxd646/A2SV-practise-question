class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
       
        seen = Counter()
        maxx = 1
        left  = 0
        for i in range(len(fruits)):
            seen[fruits[i]]+=1
            while len(seen)>2:
                seen[fruits[left]]-=1
                if seen[fruits[left]] ==0:
                    del seen[fruits[left]]
                left+=1
            maxx = max(maxx, i-left+1)
        return maxx
                


        