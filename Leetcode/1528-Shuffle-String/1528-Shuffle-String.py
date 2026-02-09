#  Shuffle String
# Platform: LeetCode
class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        meber= dict(zip(indices, list(s) ))
        return "".join(meber[i] for i in range(len(s)))     
