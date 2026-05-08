class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        rungs = [0] + rungs
        ans = 0
        for i in range(1, len(rungs)):
            x = rungs[i] - rungs[i-1]
            if x >dist:
                ans+= (x-1)//dist
        return ans
            

        