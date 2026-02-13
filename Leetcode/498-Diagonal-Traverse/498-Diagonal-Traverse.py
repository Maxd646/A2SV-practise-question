# Diagonal Traverse
# Platform: LeetCode
from typing import List
from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        count=defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                    count[i+j].append(mat[i][j])
        result=[]
        coun=1
        for ch, num in count.items():
            if coun%2!=0:
                num.reverse()
                result.extend(num)
            else:
                result.extend(num)
            coun+=1
        return result
