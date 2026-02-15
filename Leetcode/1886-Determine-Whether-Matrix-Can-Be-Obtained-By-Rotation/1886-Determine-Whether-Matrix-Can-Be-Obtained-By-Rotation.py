#  Determine Whether Matrix Can Be Obtained By Rotation
# Platform: LeetCode
from typing import List
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n= len(mat)
        for _ in range(4):
            if mat==target:
                return True
            new= [[0]*n for i in range(n)]
            for i in range(n):
                for j in range(n):
                    new[j][n-i-1]=mat[i][j]
            mat=new
        return False
