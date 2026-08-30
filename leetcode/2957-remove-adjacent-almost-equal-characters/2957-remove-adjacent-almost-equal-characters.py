class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        word = list(word)

        n = len(word)
        ans   = 0
       

        for i in range(1, n):

            if word[i] != "1" and word[i] == word[i-1] or abs(ord(word[i]) - ord(word[i-1])) ==1:

                ans += 1
                word[i] = "1"
                
        return ans
                
            
       

        return ans



        