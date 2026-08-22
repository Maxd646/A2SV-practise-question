class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        n = num
        for i in range(num+1):
            if num +int(str(num)[::-1]) == n:
                return True
            num  -= 1
        return False
        