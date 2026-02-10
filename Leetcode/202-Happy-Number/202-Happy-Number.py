# Happy Number
# Platform: LeetCode
class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        digit=0
        while n!=1:
            if n not in seen:
                seen.add(n)
                digit=sum(int(x)**2 for x in str(n))
            else:
                return False
            n=digit
        if n==1:
            return True
        else:
            return False
            
