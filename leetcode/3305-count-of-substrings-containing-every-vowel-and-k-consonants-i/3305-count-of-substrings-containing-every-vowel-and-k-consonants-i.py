class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atmost(word, k):
            if k < 0:
                return 0
            seen = Counter()
            ans = 0
            left = 0
            Vowel = 0
            const = 0
            Vowels = set("aeiou")
            last = {}

            for i in range(len(word)):
                if word[i] in Vowels:
                    last[word[i]] = i
                    if seen[word[i]] == 0:
                        Vowel += 1
                    seen[word[i]] += 1
                else:
                    const += 1

                while const > k:
                    if word[left] in Vowels:
                        seen[word[left]] -= 1
                        if seen[word[left]] ==0:
                            Vowel -= 1
                    else:
                        const -= 1
                    left += 1
                if Vowel == 5:
                    right = min(last.values())
                    ans += (right- left +1)
            return ans
        return atmost(word, k) - atmost(word, k-1)

                    
            


        