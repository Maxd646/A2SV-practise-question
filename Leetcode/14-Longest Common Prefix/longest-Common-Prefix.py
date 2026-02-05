class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_m=float("inf")
        for i in range(len(strs)):
            min_m= min(len(strs[i]), min_m)
        result= ""
        for i in range(min_m):
            match= True
            for j in range(len(strs)):
                if strs[0][i]!=strs[j][i]:
                    match= False
                    break
            if match is False:
                break
            else:
                result+=strs[0][i]
        return result