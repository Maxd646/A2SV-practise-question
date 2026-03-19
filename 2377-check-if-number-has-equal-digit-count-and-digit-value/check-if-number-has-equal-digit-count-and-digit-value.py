class Solution:
    def digitCount(self, num: str) -> bool:
        seen= Counter(map(int, num))
        for i in range(len(num)):
            if seen[i]!=int(num[i]):
                return False  
        return True
            
        