class Solution:
    def isPalindrome(self, x: int) -> bool:
        resutl=str(x)
        resut2=""
        for i in range(len(resutl)-1, -1, -1):
            resut2+=resutl[i]
        return resut2==resutl

        