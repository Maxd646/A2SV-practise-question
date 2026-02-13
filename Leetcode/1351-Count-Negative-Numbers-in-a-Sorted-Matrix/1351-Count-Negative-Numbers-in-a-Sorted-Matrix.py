# Count Negative Numbers in a Sorted Matrix
# Platform: LeetCode
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result=[]
        total=0
        for word in grid:
            result=result+word
        for i in range(len(result)):
            if result[i]<0:
                total+=1
        return total

