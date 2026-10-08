class Solution:
    def canChange(self, start: str, target: str) -> bool:

        star = [(ch, i) for i, ch in enumerate(start) if ch != "_"]
        tar = [(ch, i) for i, ch in enumerate(target) if ch != "_"]

        if len(star) != len(tar):
            return False

        for (s, i), (t, j) in zip(star, tar):

            if s != t:
                return False
            
            if t == "L" and i < j:
                return False

            if t == "R" and  j < i:
                return False

        return True

            


            






        