# Determine if Two Strings Are Close
# Platform: LeetCode

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        res1=[]
        res2=[]
        count=Counter(word1)
        for ch, num in count.items():
            res1.append(num)
        count.clear()
        count=Counter(word2)
        for ch, num in count.items():
            res2.append(num)
        return sorted(res2)==sorted(res1) and set(word1)==set(word2)
