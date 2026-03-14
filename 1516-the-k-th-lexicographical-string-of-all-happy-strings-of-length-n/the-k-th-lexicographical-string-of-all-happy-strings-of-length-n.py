class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * (2 ** (n - 1)):
            return ""

        ans = ""
        prev = ""

        for i in range(n):
            for c in "abc":
                if c == prev:
                    continue

                count = 2 ** (n - i - 1)

                if k > count:
                    k -= count
                else:
                    ans += c
                    prev = c
                    break

        return ans