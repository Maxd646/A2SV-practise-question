class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        ans = 0
        length = 0
        vowels = 0

        for i in range(len(word)):
            if i > 0 and word[i] >= word[i-1]:
                length += 1
            else:
                length = 1
                vowels = 1

            if i > 0 and word[i] > word[i-1]:
                vowels += 1
            
            if vowels == 5:
                ans = max(ans, length)

        return ans