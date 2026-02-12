# Spiral Matrix
# Platform: LeetCode
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r, c=len(matrix), len(matrix[0])
        top, bottom, right, left=0, r-1, c-1, 0
        result=[]
        while top<=bottom and left<=right:

            for i in range(left, right+1):
                result.append(matrix[top][i])
            top+=1


            for j in range(top, bottom+1):
                result.append(matrix[j][right])
            right-=1

            if top <= bottom:
                for k in range(right, left-1, -1):
                    result.append(matrix[bottom][k])
                bottom-=1
            
            if left <= right:
                for m in range(bottom, top-1, -1):
                    result.append(matrix[m][left])
                left+=1
        return result

