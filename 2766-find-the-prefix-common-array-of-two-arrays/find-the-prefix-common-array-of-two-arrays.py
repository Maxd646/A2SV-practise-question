class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        seen  = set()
        seen2 = set()
        ans = []
        for i in range(n):
            seen.add(A[i])
            seen2.add(B[i])
            ans.append(len(list(seen&seen2)))
        return ans
            




        