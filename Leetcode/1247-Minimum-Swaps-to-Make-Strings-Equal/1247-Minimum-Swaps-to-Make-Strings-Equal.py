# Minimum Swaps to Make Strings Equal
# Platform: LeetCode

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if len(s1)!=len(s2):
            return -1
        result=0
        if s1==s2:
            return 0
        ax, ay=0, 0
        for a, b in zip(s1, s2):
            if a!=b:
                if a=="x":
                    ax+=1
                else:
                    ay+=1
        if (ay+ax)%2!=0:
            return -1
        result=ay//2+ax//2
        if ax%2==1:
            result+=2

        return result
