#  Image Smoother
# Platform: LeetCode
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        result= [[0]*len(img[0]) for _ in range(len(img))]
        nav=  [(-1,-1), (-1,0), (-1,1), (0,-1),  (0,0),  (0,1),(1,-1),  (1,0),  (1,1)]
        for i in range(len(img)):
            for j in range(len(img[0])):
                summ = 0
                no = 0
                for x, y in nav:
                    ii, jj = i + x, j + y
                    
                    if 0 <= ii < len(img) and 0 <= jj < len(img[0]):
                        summ+= img[ii][jj]
                        no += 1
                result[i][j] = summ// no
        
        return result
