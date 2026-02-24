# Partition Labels
# Platform: LeetCode

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        left, right=0, 0
        pre=[0]
        m=0
        while right<len(s):
            while right<=s.rindex(s[left]):
                m=max(s.rindex(s[right]), m)
                left=m
                right+=1
            pre.append(m+1)
            left=m+1
            right=m+1
        ans=[pre[i+1]-pre[i] for i in range(len(pre)-1)]
        return ans 

