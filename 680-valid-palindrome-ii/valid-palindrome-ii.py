class Solution:
    def validPalindrome(self, s: str) -> bool:
        j=0
        found =False
        rev=s[::-1]
        for i in range(len(s)):
            if rev[i] != s[i]:
                j=i
                found=True
                break
        if not found:
            return True

        else:
            
            opt2=s[:i]+s[i+1:]
            opt1=rev[:i]+rev[i+1:]
            return opt1==opt1[::-1] or opt2==opt2[::-1] 

        
        