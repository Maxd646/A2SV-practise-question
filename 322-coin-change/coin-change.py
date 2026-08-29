class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}
        result = float("inf")

        def dfs(amount):

            if amount == 0:
                return 0

            if amount not in memo:
                result = float("inf")

                for coin in coins:
                    if coin <= amount:
                        result = min(result, dfs(amount - coin) + 1)

                memo[amount] = result

            return memo[amount]
            
        ans = dfs(amount)

        if ans != float("inf"):
            return ans
        return -1

            