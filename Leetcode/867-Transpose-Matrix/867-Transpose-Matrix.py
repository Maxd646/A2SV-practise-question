# Transpose Matrix
# Platform: LeetCode
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result= []
        for i in range(len(matrix[0])):
            new=[]
            for j in range(len(matrix)):
                new.append(matrix[j][i])
            result.append(new)
        return result
