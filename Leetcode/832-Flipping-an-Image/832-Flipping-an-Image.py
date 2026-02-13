# Flipping an Image
# Platform: LeetCode
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result =[list(reversed(num)) for num in image]
        for i in range(len(image)):
            for j in range(len(image)):
                if result[i][j]==1:
                    result[i][j]=0
                else:
                    result[i][j]=1
        return result
