class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        answer = max(special[0] - bottom, top - special[-1])
        for i in range(1, len(special)):
            gap = special[i] - special[i-1] - 1
            answer = max(answer, gap)
        
        return answer