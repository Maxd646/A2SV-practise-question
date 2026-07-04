class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            count = 0
            seen = set()
            for j in range(len(matrix)):
                if matrix[i][j] not in seen:
                    count+=1
                seen.add(matrix[i][j])
            if count!=len(matrix):
                return False
            count = 0
            seen = set()
            
            for j in range(len(matrix)):
                if matrix[j][i] not in seen:
                    count+=1
                seen.add(matrix[j][i])
            if count!=len(matrix):
                return False
        return True

        