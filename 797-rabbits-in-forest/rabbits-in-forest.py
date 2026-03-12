class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        res = 0

        for x, c in count.items():
            groups = (c + x ) // (x+1)
            res += groups * (x+1)

        return res


        