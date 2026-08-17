class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def back(x, path):

            if len(path) == k:
                ans.append(path[:])
                return 
            for i in range(x, n+1):
                path.append(i)
                back(i+1, path)
                path.pop()
        ans = []
        back(1, [])
        return ans


        