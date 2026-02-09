# Find Three Consecutive Integers That Sum to a Given Number
# Platform: LeetCode

class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        return [] if num%3!=0 else [num//3-1, num//3, num//3+1]
               
