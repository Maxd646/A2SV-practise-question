class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans=0
        seen= Counter(s)
        odd=False
        for key, value in seen.items():
            if value%2==0:
                ans+=value
            else:
                ans+=(value-1)
                odd=True
        if odd:
            ans+=1
        return ans
        


        