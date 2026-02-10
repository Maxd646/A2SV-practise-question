# Minimum Number of Steps to Make Two Strings Anagram
# Platform: LeetCode

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        need= Counter(t)-Counter(s)
        summ=0
        for ch, num in need.items():
            summ+=num
        return summ
