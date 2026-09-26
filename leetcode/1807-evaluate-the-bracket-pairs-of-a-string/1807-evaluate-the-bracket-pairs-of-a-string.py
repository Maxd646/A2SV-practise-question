class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:

        seen = {word: val for word, val in knowledge}

        res = ""

        yes = False
        key = ""

        for i in range(len(s)):

            if s[i] == ")":

                res += seen.get(key, "?")
                key = ""
                yes = False
                continue

            if s[i] == "(":

                yes = True
                continue

            if yes:

                key += s[i]
                continue

            res += s[i]

        return res



            

            

        