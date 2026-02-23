# Divide Players Into Teams of Equal Skill
# Platform: LeetCode
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        equl= skill[0]+skill[-1]
        ans=0
        for i in range(len(skill)//2):
            if skill[i]+skill[-(i+1)]==equl:
                ans+=skill[i]*skill[-(i+1)]
            else:
                return -1 
        return ans
