class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0

        for ch in s:
            if ch == "[":
                balance += 1
                
            elif balance > 0:
                balance -= 1

        return (balance + 1) // 2