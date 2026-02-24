# Sum of Square Numbers
# Platform: LeetCode
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(c**0.5)+1):
            a= c-(i**2)
            if a**0.5==math.ceil(a**0.5) and a>=0:
                return True
        return False

