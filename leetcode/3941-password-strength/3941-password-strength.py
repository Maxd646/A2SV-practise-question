class Solution:
    def passwordStrength(self, password: str) -> int:

        ans = 0
        seen = set()
        for ch in password:

            if ch in seen: continue 
            seen.add(ch)

            if ch in "!@#$":

                ans += 5

            elif ch in "0123456789":

                ans += 3

            elif 65 <= ord(ch) <= 90:

                ans += 2

            elif 97 <= ord(ch) <= 122:

                ans += 1

            else: ans += 0

        return ans 
        