class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            
            n = len(mat)
            rot= [[0]*n for _ in range(n)]
            
            for i in range(n):
                for j in range(n):
                    rot[j][n - 1 - i] = mat[i][j]
            
            mat = rot
    
        return False