class Solution:
    def addMinimum(self, word: str) -> int:

        n = len(word)
        words = "abc"*n

        left = 0
        ans = 0

        for i in range(len(words)):

            if words[i]  == word[left]:
                left += 1
            else:
                ans += 1

            if left == n:

                if word[left-1] == "a":
                    return ans +2

                if word[left-1] == "b":
                    return ans +1

                return ans

        return ans 
            


        