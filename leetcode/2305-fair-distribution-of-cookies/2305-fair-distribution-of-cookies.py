class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        seen = {tuple([0] * k)}

        for num in cookies:
            poss = set()

            for state in seen:
                for i in range(k):
                    new_state = list(state)
                    new_state[i] += num
                    poss.add(tuple(sorted(new_state)))

            seen = poss

        ans = float('inf')
        for state in seen:
            ans = min(ans, max(state))

        return ans
    

        