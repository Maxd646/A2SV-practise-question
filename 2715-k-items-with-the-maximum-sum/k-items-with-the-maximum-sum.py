class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        num= [1]*numOnes+[0]*numZeros+[-1]*numNegOnes
        print(num)
        return sum(num[:k])
        