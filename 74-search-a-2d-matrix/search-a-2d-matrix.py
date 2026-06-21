class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(mat, x):
            n = len(mat)
            l, r = 0, n-1
            while l<=r:
                mid = l+(r-l)//2
                if mat[mid] == x:
                    return True
                elif mat[mid]<x:
                    l = mid+1
                else: r = mid -1
            return False
        n = len(matrix)-1
        row  = -1
        l, r = 0, n
        x = target
        while l<=r:
            mid = l +(r-l)//2
            if x == matrix[mid][0]:
                return True
            elif matrix[mid][0]<x:
                row = mid 
                l = mid +1
            else:
                r = mid -1
        if row == -1:
            return False
        return search(matrix[row], target)
        
    
        