# Ransom Note
# Platform: LeetCode
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count=Counter(magazine)
        coun=Counter(ransomNote)
        for i in range(len(ransomNote)):
            if coun[ransomNote[i]]>count[ransomNote[i]]:
                return False
        return True  
