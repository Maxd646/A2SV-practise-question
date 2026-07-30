class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum((i+8)//8 for i in range(len(word)))
        