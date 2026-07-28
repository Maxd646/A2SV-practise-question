class Solution:
    def smallestPalindrome(self, s: str) -> str:
        letter = list(s)
        letter.sort()
        seen = Counter(letter)
        ans = ["-"]*len(s)
        l =0
        for ch, num in seen.items():
            if num%2 !=0:
                ans[len(s)//2] = ch
            for i in range(num//2):
                ans[l] = ch
                ans[len(s)-l-1] = ch
                l+=1
        return "".join(ans)

        