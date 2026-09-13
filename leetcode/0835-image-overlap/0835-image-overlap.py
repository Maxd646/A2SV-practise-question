class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:


        n = len(img1)
        arr1 = []
        arr2 = []

        for i in range(n):

            for j in range(n):

                if img1[i][j] == 1:
                    arr1.append((i, j))

                if img2[i][j] == 1:
                    arr2.append((i, j))
        
        seen = Counter()
        ans = 0

        for i, j in arr1:

            for r, c in arr2:

                diff = (r-i, c-j)
                seen[diff] += 1
                ans = max(ans, seen[diff])

        return ans


        