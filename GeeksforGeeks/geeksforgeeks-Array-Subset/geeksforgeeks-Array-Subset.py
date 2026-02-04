# Array Subset

from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        A=Counter(a)
        B=Counter(b)
        for m, num in B.items():
            if num > A.get(m, 0):
                return False
        return True

        
    